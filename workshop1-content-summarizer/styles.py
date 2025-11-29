"""Custom CSS styles for the app"""

CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
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
    }
    
    .summary-content {
        font-family: 'Inter', sans-serif;
        color: #374151;
        line-height: 1.75;
    }
    
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
    
    .preview-content {
        font-family: 'Inter', sans-serif;
        color: #6b7280;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    .stButton > button {
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 14px 0 rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(102, 126, 234, 0.5) !important;
    }
    
    .stTextInput > div > div > input {
        border-radius: 12px !important;
        border: 2px solid #e5e7eb !important;
        padding: 0.75rem 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
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
    }
    
    .stRadio > div > label:hover {
        border-color: #667eea !important;
        background: #f5f3ff !important;
    }
    
    .section-label {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        color: #374151;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #9ca3af;
        font-size: 0.85rem;
    }
    
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #e5e7eb, transparent);
        margin: 1.5rem 0;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
