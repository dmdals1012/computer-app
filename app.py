
import streamlit as st
from home import show_home
# from description import show_description
# from ml import show_ml

st.set_page_config(page_title="컴퓨터 부품 추천 시스템", layout="wide")

pages = {
    "홈": show_home,
  #  "시스템 설명": show_description,
  #  "부품 추천": show_ml
}

st.sidebar.title("메뉴")
selection = st.sidebar.radio("페이지 선택", list(pages.keys()))

pages[selection]()
