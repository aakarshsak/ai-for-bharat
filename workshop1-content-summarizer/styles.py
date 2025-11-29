"""
CSS Styles for Content Summarizer App
"""

def get_css_styles():
    """Return the CSS styles for the application."""
    return """
<style>
    /* Import clean fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 1.5rem 0;
        margin-bottom: 1rem;
    }
    
    .main-header h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        font-family: 'Inter', sans-serif;
        color: #6b7280;
        font-size: 1.1rem;
    }
    
    /* Card styling */
    .card {
        background: #ffffff;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
    }
    
    .card-dark {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
        color: white;
    }
    
    /* Summary result styling */
    .summary-card {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-radius: 16px;
        padding: 1.5rem;
        border-left: 4px solid #22c55e;
        margin-top: 1rem;
    }
    
    .summary-title {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.2rem;
        color: #166534;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .summary-content {
        font-family: 'Inter', sans-serif;
        color: #374151;
        font-size: 1rem;
        line-height: 1.75;
    }
    
    /* Error styling */
    .error-card {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        border-radius: 16px;
        padding: 1.5rem;
        border-left: 4px solid #ef4444;
        margin-top: 1rem;
    }
    
    .error-content {
        font-family: 'Inter', sans-serif;
        color: #991b1b;
        font-size: 0.95rem;
    }
    
    /* Preview styling */
    .preview-card {
        background: #f9fafb;
        border-radius: 12px;
        padding: 1rem;
        border: 1px dashed #d1d5db;
        margin-top: 1rem;
    }
    
    .preview-content {
        font-family: 'Inter', sans-serif;
        color: #6b7280;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        font-size: 1rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 14px 0 rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(102, 126, 234, 0.5) !important;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 12px !important;
        border: 2px solid #e5e7eb !important;
        padding: 0.75rem 1rem !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        transition: border-color 0.2s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Radio button styling */
    .stRadio > div {
        gap: 1rem;
    }
    
    .stRadio > div > label {
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        padding: 0.75rem 1.25rem !important;
        border-radius: 10px !important;
        border: 2px solid #e5e7eb !important;
        background: white !important;
        transition: all 0.2s ease !important;
    }
    
    .stRadio > div > label:hover {
        border-color: #667eea !important;
        background: #f5f3ff !important;
    }
    
    /* Section labels */
    .section-label {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        color: #374151;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        font-family: 'Inter', sans-serif;
        color: #9ca3af;
        font-size: 0.85rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #e5e7eb, transparent);
        margin: 1.5rem 0;
    }
</style>
"""

