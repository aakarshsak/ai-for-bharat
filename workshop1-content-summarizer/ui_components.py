"""
UI Components for Content Summarizer App
Reusable HTML templates for the application.
"""


def get_header():
    """Return the main header HTML."""
    return """
<div class="main-header">
    <h1>📝 Content Summarizer</h1>
    <p>Transform any blog, article, or post into a crisp summary</p>
</div>
"""


def get_divider():
    """Return a divider HTML element."""
    return '<div class="divider"></div>'


def get_section_label(icon: str, text: str):
    """Return a section label HTML."""
    return f'<p class="section-label">{icon} {text}</p>'


def get_spacer():
    """Return a line break for spacing."""
    return "<br>"


def get_summary_card(title: str, summary: str):
    """Return a success summary card HTML."""
    return f"""
<div class="summary-card">
    <div class="summary-title">
        ✅ {title}
    </div>
    <div class="summary-content">
        {summary}
    </div>
</div>
"""


def get_error_card(title: str, message: str, error_details: str = None):
    """Return an error card HTML."""
    error_html = f"""
<div class="error-card">
    <div class="error-content">
        <strong>{title}</strong><br>
        {message}
"""
    if error_details:
        error_html += f"<br><br><code>{error_details}</code>"
    
    error_html += """
    </div>
</div>
"""
    return error_html


def get_preview_content(content: str):
    """Return preview content HTML."""
    return f"""
<div class="preview-content">
    {content}
</div>
"""


def get_footer():
    """Return the footer HTML."""
    return """
<div class="footer">
    Powered by Amazon Bedrock & Claude ⚡
</div>
"""

