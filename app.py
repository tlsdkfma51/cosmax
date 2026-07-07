import pathlib

import streamlit as st
import streamlit.components.v1 as components

# ── 기본 페이지 설정 ─────────────────────────────────────────
st.set_page_config(
    page_title="브리프드래프트 BriefDraft",
    page_icon="📝",
    layout="wide",
)

# Streamlit 기본 여백/헤더를 최소화해서 index.html 디자인이 그대로 보이도록 처리
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── index.html 로드 ─────────────────────────────────────────
HTML_PATH = pathlib.Path(__file__).parent / "index.html"
html_content = HTML_PATH.read_text(encoding="utf-8")

# 이 앱은 순수 프론트엔드(JS)로 동작하는 정적 페이지이므로
# components.html로 그대로 렌더링합니다. (백엔드 API 호출 없음)
components.html(html_content, height=1400, scrolling=True)
