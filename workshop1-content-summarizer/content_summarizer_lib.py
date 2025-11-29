import boto3
import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# Common content selectors for blog/article pages
CONTENT_SELECTORS = [
    'article', '[role="main"]', '.post-content', '.article-content',
    '.entry-content', '.content', 'main', '.blog-post', '.post-body'
]


def fetch_content(url):
    """Fetch and extract text content from a URL"""
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    # Remove junk elements
    for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
        tag.decompose()
    
    # Find main content
    content = None
    for selector in CONTENT_SELECTORS:
        content = soup.select_one(selector)
        if content:
            break
    
    if not content:
        content = soup.body or soup
    
    text = content.get_text(separator='\n', strip=True)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    
    # Truncate if too long
    if len(text) > 15000:
        text = text[:15000] + "..."
    
    return text


def get_title(url):
    """Extract page title from URL"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(resp.content, 'html.parser')
        
        og = soup.find('meta', property='og:title')
        if og and og.get('content'):
            return og['content']
        
        return soup.title.string if soup.title else "Untitled"
    except:
        return "Untitled"


def get_summary(content, summary_type):
    """Generate summary using Bedrock"""
    if summary_type == "one_line":
        prompt = f"Give a 1-2 sentence summary of this:\n\n{content}"
    else:
        prompt = f"Summarize this in 2-3 paragraphs, covering the main points:\n\n{content}"

    bedrock = boto3.Session().client('bedrock-runtime')
    
    response = bedrock.converse(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig={"maxTokens": 1000, "temperature": 0.3}
    )
    
    return response['output']['message']['content'][0]['text']


def summarize_url(url, summary_type):
    """Main function - fetch URL and return summary"""
    content = fetch_content(url)
    title = get_title(url)
    summary = get_summary(content, summary_type)
    
    preview = content[:500] + "..." if len(content) > 500 else content
    
    return {"title": title, "summary": summary, "content_preview": preview}
