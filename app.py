import streamlit as st

from ui.research_page import render_research


st.set_page_config(
    page_title="AI Research Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

render_research()
