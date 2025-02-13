
import streamlit as st

def show_home():
    st.title("컴퓨터 부품 추천 시스템에 오신 것을 환영합니다!")
    
    st.write("""
    이 시스템은 사용자의 요구사항에 맞는 최적의 컴퓨터 부품을 추천해드립니다.
    
    사용 방법:
    1. 왼쪽 사이드바에서 원하는 페이지를 선택하세요.
    2. '시스템 설명' 페이지에서 자세한 사용 방법을 확인할 수 있습니다.
    3. '부품 추천' 페이지에서 실제 추천을 받아보세요.
    """)
    
    st.image("https://example.com/computer_parts_image.jpg", caption="다양한 컴퓨터 부품들")

    st.subheader("시스템 특징")
    st.write("""
    - 최신 부품 데이터베이스 활용
    - 사용자 맞춤형 추천 알고리즘
    - 가격대비 성능 최적화
    - 호환성 검증
    """)
