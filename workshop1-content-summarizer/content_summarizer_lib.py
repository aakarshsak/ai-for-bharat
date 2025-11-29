import boto3
import requests
from bs4 import BeautifulSoup
import re


def fetch_content_from_url(url: str) -> str:
    """
    Fetch and extract readable text content from a given URL.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Remove script and style elements
    for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'advertisement']):
        element.decompose()
    
    # Try to find main content areas first
    main_content = None
    content_selectors = [
        'article',
        '[role="main"]',
        '.post-content',
        '.article-content',
        '.entry-content',
        '.content',
        'main',
        '.blog-post',
        '.post-body'
    ]
    
    for selector in content_selectors:
        main_content = soup.select_one(selector)
        if main_content:
            break
    
    # Fall back to body if no main content found
    if not main_content:
        main_content = soup.body if soup.body else soup
    
    # Extract text
    text = main_content.get_text(separator='\n', strip=True)
    
    # Clean up extra whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    
    # Limit content length to avoid token limits (roughly 15000 characters)
    if len(text) > 15000:
        text = text[:15000] + "...[content truncated]"
    
    return text


def get_title_from_url(url: str) -> str:
    """
    Extract the title from a URL.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to get title from meta tags first
        og_title = soup.find('meta', property='og:title')
        if og_title and og_title.get('content'):
            return og_title['content']
        
        # Fall back to title tag
        if soup.title:
            return soup.title.string
        
        return "Content"
    except Exception:
        return "Content"


def get_summary(content: str, summary_type: str) -> str:
    """
    Generate a summary of the content using Amazon Bedrock.
    
    Args:
        content: The text content to summarize
        summary_type: Either "one_line" or "detailed"
    """
    
    if summary_type == "one_line":
        prompt = f"""Please provide a single, concise one-line summary (maximum 2 sentences) of the following content. 
The summary should capture the main point or takeaway.

Content:
{content}

One-line summary:"""
    else:
        prompt = f"""Please provide a detailed summary of the following content in 2-3 paragraphs.
The summary should:
- Cover the main ideas and key points
- Maintain the logical flow of the original content
- Be informative yet concise

Content:
{content}

Detailed summary:"""

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    message = {
        "role": "user",
        "content": [{"text": prompt}]
    }
    
    response = bedrock.converse(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=[message],
        inferenceConfig={
            "maxTokens": 1000,
            "temperature": 0.3,
            "topP": 0.9,
        },
    )
    
    return response['output']['message']['content'][0]['text']


def summarize_url(url: str, summary_type: str) -> dict:
    """
    Main function to fetch content from URL and generate summary.
    
    Returns:
        dict with 'title', 'summary', and 'content_preview' keys
    """
    # Fetch content
    content = fetch_content_from_url(url)
    title = get_title_from_url(url)
    
    # Generate summary
    summary = get_summary(content, summary_type)
    
    return {
        "title": title,
        "summary": summary,
        "content_preview": content[:500] + "..." if len(content) > 500 else content
    }

