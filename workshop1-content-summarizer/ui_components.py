"""HTML components for the summarizer UI"""

HEADER = """
<div class="main-header">
    <h1>📝 Content Summarizer</h1>
    <p>Transform any blog, article, or post into a crisp summary</p>
</div>
"""

DIVIDER = '<div class="divider"></div>'

FOOTER = """
<div class="footer">
    Powered by Amazon Bedrock & Claude ⚡
</div>
"""


def section_label(icon, text):
    return f'<p class="section-label">{icon} {text}</p>'


def summary_card(title, summary):
    return f"""
    <div class="summary-card">
        <div class="summary-title">✅ {title}</div>
        <div class="summary-content">{summary}</div>
    </div>
    """


def error_card(title, message, details=None):
    html = f"""
    <div class="error-card">
        <div class="error-content">
            <strong>{title}</strong><br>{message}
    """
    if details:
        html += f"<br><br><code>{details}</code>"
    html += "</div></div>"
    return html


def preview_box(content):
    return f'<div class="preview-content">{content}</div>'
