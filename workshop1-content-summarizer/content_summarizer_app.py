"""
Content Summarizer App
A Streamlit application that summarizes blog posts and articles using Amazon Bedrock.
"""

import streamlit as st
import requests

# Local imports
import content_summarizer_lib as glib
from styles import get_css_styles
from ui_components import (
    get_header,
    get_divider,
    get_section_label,
    get_spacer,
    get_summary_card,
    get_error_card,
    get_preview_content,
    get_footer
)


# ============================================
# Page Configuration
# ============================================
st.set_page_config(
    page_title="Content Summarizer",
    page_icon="📝",
    layout="centered"
)


# ============================================
# Apply Custom Styles
# ============================================
st.markdown(get_css_styles(), unsafe_allow_html=True)


# ============================================
# Header Section
# ============================================
st.markdown(get_header(), unsafe_allow_html=True)
st.markdown(get_divider(), unsafe_allow_html=True)


# ============================================
# URL Input Section
# ============================================
st.markdown(get_section_label("🔗", "Paste URL"), unsafe_allow_html=True)
url_input = st.text_input(
    "URL",
    placeholder="https://example.com/blog/your-article",
    label_visibility="collapsed"
)

st.markdown(get_spacer(), unsafe_allow_html=True)


# ============================================
# Summary Type Selection
# ============================================
st.markdown(get_section_label("⚙️", "Choose Summary Type"), unsafe_allow_html=True)
summary_type = st.radio(
    "Summary Type",
    options=["one_line", "detailed"],
    format_func=lambda x: "📌 Quick Summary (1-2 sentences)" if x == "one_line" else "📖 Detailed Summary (2-3 paragraphs)",
    label_visibility="collapsed",
    horizontal=True
)

st.markdown(get_spacer(), unsafe_allow_html=True)


# ============================================
# Generate Button
# ============================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    summarize_button = st.button(
        "✨ Generate Summary", 
        type="primary", 
        use_container_width=True
    )


# ============================================
# Process and Display Results
# ============================================
if summarize_button:
    # Validate URL input
    if not url_input:
        st.markdown(
            get_error_card(
                "⚠️ Missing URL",
                "Please enter a valid URL to summarize."
            ),
            unsafe_allow_html=True
        )
    elif not url_input.startswith(('http://', 'https://')):
        st.markdown(
            get_error_card(
                "⚠️ Invalid URL Format",
                "Please enter a complete URL starting with http:// or https://"
            ),
            unsafe_allow_html=True
        )
    else:
        # Process the URL
        with st.spinner("🔄 Fetching content and generating summary..."):
            try:
                # Get summary from the backend
                result = glib.summarize_url(url_input, summary_type)
                
                # Display summary result
                st.markdown(
                    get_summary_card(result['title'], result['summary']),
                    unsafe_allow_html=True
                )
                
                # Show content preview in expander
                with st.expander("👀 View Extracted Content Preview"):
                    st.markdown(
                        get_preview_content(result['content_preview']),
                        unsafe_allow_html=True
                    )
                
            except requests.exceptions.RequestException as e:
                st.markdown(
                    get_error_card(
                        "❌ Failed to fetch content",
                        "Could not retrieve content from the provided URL.",
                        str(e)
                    ),
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.markdown(
                    get_error_card(
                        "❌ Error occurred",
                        "Something went wrong while processing your request.",
                        str(e)
                    ),
                    unsafe_allow_html=True
                )


# ============================================
# Footer
# ============================================
st.markdown(get_footer(), unsafe_allow_html=True)
