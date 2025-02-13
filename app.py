import streamlit as st
from PIL import Image
from datetime import datetime, timedelta
import pandas as pd

# from ui.description import app_description
from util.home import show_home
from util.ml import show_recommendation, EnsembleModel

class EnsembleModel(BaseEstimator, RegressorMixin):
    def __init__(self, knn_model, svd_model, knn_weight=0.5):
        self.knn_model = knn_model
        self.svd_model = svd_model
        self.knn_weight = knn_weight

    def fit(self, X, y):
        self.knn_model.fit(X, y)
        self.svd_model.fit(X)
        return self

    def predict(self, X):
        knn_pred = self.knn_model.predict(X)
        svd_pred = self.svd_model.inverse_transform(self.svd_model.transform(X))[:, 0]
        return self.knn_weight * knn_pred + (1 - self.knn_weight) * svd_pred


def sidebar():
    st.sidebar.title("🖥️ 컴퓨터 부품 추천 시스템 🛠️")

    st.sidebar.markdown("---")

    pages = {
        "🏠 홈": show_home,
     #   "📖 앱 소개": app_description,
        "🎯 부품 추천": show_recommendation,
     #   "📊 데이터 분석": lambda: data_analysis_page()
    }
    
    choice = st.sidebar.radio("메뉴 선택", list(pages.keys()))



def main():
    choice = sidebar()

    if choice == "🏠 홈":
        show_home()
  #  elif choice == "📖 앱 소개":
   #     app_description()
    elif choice == "🎯 부품 추천":
        show_recommendation()
   # elif choice == "📊 데이터 분석":
    #    data_analysis_page()

if __name__ == '__main__':
    main()
