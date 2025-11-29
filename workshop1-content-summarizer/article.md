# Build a URL Post Summarizer Using Amazon Bedrock and Streamlit

**Level**: Intermediate  
**Time to complete**: 30 minutes  
**Services used**: Amazon Bedrock, Claude 3.5 Sonnet

---

## Overview

In this tutorial, you'll build a web application that summarizes content from any public URL using Amazon Bedrock and Claude 3.5 Sonnet. The app extracts text from blog posts, articles, and web pages, then generates AI-powered summaries in two formats: a quick 1-2 sentence overview or a detailed multi-paragraph breakdown.

By the end of this tutorial, you'll have a working Streamlit application that demonstrates how to integrate Amazon Bedrock's Converse API for text summarization use cases.

---

## Prerequisites

Before you begin, ensure you have:

- An AWS account with Amazon Bedrock access enabled
- Claude 3.5 Sonnet model access in your AWS region
- Python 3.8+ installed
- AWS CLI configured with appropriate credentials
- Basic familiarity with Python and Streamlit

---

## What You'll Build

A URL post summarizer application with the following features:

- URL input for any public webpage
- Two summarization modes (quick and detailed)
- Clean, modern web interface
- Content preview functionality

![Application Interface](screenshots/request.png)

---

## Architecture

The application follows a simple three-tier architecture:

```
User Browser → Streamlit App → Target Website
                    ↓
              Amazon Bedrock
              (Claude 3.5 Sonnet)
```

1. **User inputs a URL** through the Streamlit interface
2. **Content extraction** fetches and parses the webpage using BeautifulSoup
3. **AI summarization** sends the content to Amazon Bedrock
4. **Results display** shows the generated summary to the user

---

## Step 1: Set Up Your Project

Create a new directory and install the required dependencies:

```bash
mkdir content-summarizer
cd content-summarizer
```

Create a `requirements.txt` file:

```
streamlit
boto3
botocore
requests
beautifulsoup4
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 2: Build the Content Extraction Module

Create `content_summarizer_lib.py` to handle URL fetching and AI summarization:

```python
import boto3
import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

CONTENT_SELECTORS = [
    'article', '[role="main"]', '.post-content', '.article-content',
    '.entry-content', '.content', 'main', '.blog-post', '.post-body'
]


def fetch_content(url):
    """Fetch and extract text content from a URL"""
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    # Remove non-content elements
    for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
        tag.decompose()
    
    # Find main content using common selectors
    content = None
    for selector in CONTENT_SELECTORS:
        content = soup.select_one(selector)
        if content:
            break
    
    if not content:
        content = soup.body or soup
    
    text = content.get_text(separator='\n', strip=True)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Truncate if too long for model context
    if len(text) > 15000:
        text = text[:15000] + "..."
    
    return text
```

The `fetch_content` function:
- Fetches the webpage with a browser-like User-Agent
- Removes scripts, styles, and navigation elements
- Uses common CSS selectors to find the main content area
- Cleans up whitespace and truncates long content

---

## Step 3: Integrate Amazon Bedrock

Add the summarization function to `content_summarizer_lib.py`:

```python
def get_summary(content, summary_type):
    """Generate summary using Amazon Bedrock"""
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
    summary = get_summary(content, summary_type)
    preview = content[:500] + "..." if len(content) > 500 else content
    
    return {"summary": summary, "content_preview": preview}
```

Key points about the Bedrock integration:
- Uses the **Converse API** for simplified model interaction
- Sets `temperature: 0.3` for consistent, focused outputs
- Limits `maxTokens: 1000` to control response length

---

## Step 4: Create the Streamlit Interface

Create `content_summarizer_app.py`:

```python
import streamlit as st
import requests
import content_summarizer_lib as glib

st.set_page_config(page_title="URL Post Summarizer", page_icon="📝", layout="centered")

st.title("📝 URL Post Summarizer")
st.write("Transform any blog, article, or post into a crisp summary")

# URL input
url = st.text_input("Paste URL", placeholder="https://example.com/blog/article")

# Summary type selection
summary_type = st.radio(
    "Choose Summary Type",
    ["one_line", "detailed"],
    format_func=lambda x: "📌 Quick Summary (1-2 sentences)" if x == "one_line" 
                          else "📖 Detailed Summary (2-3 paragraphs)",
    horizontal=True
)

# Generate button
if st.button("✨ Generate Summary", type="primary"):
    if not url or not url.startswith(('http://', 'https://')):
        st.error("Please enter a valid URL starting with http:// or https://")
    else:
        with st.spinner("Fetching and summarizing..."):
            try:
                result = glib.summarize_url(url, summary_type)
                st.success("Summary generated!")
                st.write(result['summary'])
                
                with st.expander("View extracted content"):
                    st.write(result['content_preview'])
                    
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to fetch URL: {e}")
            except Exception as e:
                st.error(f"Error: {e}")
```

---

## Step 5: Configure IAM Permissions

Ensure your AWS credentials have the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:Converse"
            ],
            "Resource": "*"
        }
    ]
}
```

---

## Step 6: Run the Application

Start the Streamlit app:

```bash
streamlit run content_summarizer_app.py
```

Open your browser to `http://localhost:8501` and test with any public article URL.

![Summary Results](screenshots/result1.png)

---

## How It Works

1. **URL Submission**: User pastes a blog or article URL
2. **Content Extraction**: BeautifulSoup parses the HTML and extracts the main text content, removing navigation, ads, and scripts
3. **Prompt Construction**: Based on the selected summary type, a specific prompt is built
4. **Bedrock Inference**: The content and prompt are sent to Claude 3.5 Sonnet via the Converse API
5. **Result Display**: The generated summary is shown to the user

---

## Conclusion

You've built a functional URL post summarizer using Amazon Bedrock and Streamlit. This pattern can be extended for various use cases:

- **Research assistants** that summarize academic papers
- **News aggregators** with AI-generated briefs
- **Content curation tools** for newsletters
- **Competitive analysis** applications

The Amazon Bedrock Converse API simplifies integration with foundation models, making it easy to add AI capabilities to your applications.

---

## Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Bedrock Converse API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Source Code on GitHub](https://github.com/aakarshsak/ai-for-bharat/tree/master/workshop1-content-summarizer)

---

## Clean Up

To avoid ongoing charges, stop the Streamlit application when you're done testing. Amazon Bedrock charges are based on usage, so no additional cleanup is required for the AI service.
