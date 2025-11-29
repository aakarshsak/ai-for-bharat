import streamlit as st
import requests
import content_summarizer_lib as glib
from styles import CSS
from ui_components import (
    HEADER, DIVIDER, FOOTER,
    section_label, summary_card, error_card, preview_box
)

st.set_page_config(page_title="Content Summarizer", page_icon="📝", layout="centered")
st.markdown(CSS, unsafe_allow_html=True)

# Header
st.markdown(HEADER, unsafe_allow_html=True)
st.markdown(DIVIDER, unsafe_allow_html=True)

# URL input
st.markdown(section_label("🔗", "Paste URL"), unsafe_allow_html=True)
url = st.text_input("URL", placeholder="https://example.com/blog/article", label_visibility="collapsed")
st.markdown("<br>", unsafe_allow_html=True)

# Summary type
st.markdown(section_label("⚙️", "Choose Summary Type"), unsafe_allow_html=True)
summary_type = st.radio(
    "Type",
    ["one_line", "detailed"],
    format_func=lambda x: "📌 Quick Summary (1-2 sentences)" if x == "one_line" else "📖 Detailed Summary (2-3 paragraphs)",
    label_visibility="collapsed",
    horizontal=True
)
st.markdown("<br>", unsafe_allow_html=True)

# Button
_, btn_col, _ = st.columns([1, 2, 1])
with btn_col:
    clicked = st.button("✨ Generate Summary", type="primary", use_container_width=True)

# Handle submission
if clicked:
    if not url:
        st.markdown(error_card("⚠️ Missing URL", "Please enter a URL to summarize."), unsafe_allow_html=True)
    elif not url.startswith(('http://', 'https://')):
        st.markdown(error_card("⚠️ Invalid URL", "URL must start with http:// or https://"), unsafe_allow_html=True)
    else:
        with st.spinner("Fetching and summarizing..."):
            try:
                result = glib.summarize_url(url, summary_type)
                st.markdown(summary_card(result['title'], result['summary']), unsafe_allow_html=True)
                
                with st.expander("👀 View extracted content"):
                    st.markdown(preview_box(result['content_preview']), unsafe_allow_html=True)
                    
            except requests.exceptions.RequestException as e:
                st.markdown(error_card("❌ Fetch failed", "Couldn't load the URL.", str(e)), unsafe_allow_html=True)
            except Exception as e:
                st.markdown(error_card("❌ Error", "Something went wrong.", str(e)), unsafe_allow_html=True)

st.markdown(FOOTER, unsafe_allow_html=True)
