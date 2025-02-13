
import pandas as pd
import numpy as np
import joblib
import streamlit as st
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.neighbors import KNeighborsRegressor
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

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

# 모델 로드
pipeline = joblib.load('model/pipeline.pkl')

# 데이터 로드
df = pd.read_csv("data/dataset.csv")

def get_user_input():
    st.title("컴퓨터 부품 추천 시스템")
    
    budget = st.slider("예산을 입력하세요 ($)", 500, 5000, 1000)
    size = st.slider("원하는 팬 크기 (mm)", 60, 200, 120)
    airflow = st.slider("원하는 공기 흐름 (CFM)", 0, 200, 50)
    noise = st.slider("허용 가능한 소음 수준 (dBA)", 0, 50, 25)
    
    return budget, size, airflow, noise

def recommend_parts(budget, size, airflow, noise):
    # 사용자 입력을 모델 입력 형식으로 변환
    user_input = np.array([[size, airflow, noise]])
    
    # 모델을 사용하여 예측
    predicted_price = pipeline.predict(user_input)[0]
    
    # 예산 내에서 가장 적합한 부품 찾기
    suitable_parts = df[(df['price'] <= budget) & (df['price'] >= predicted_price * 0.8)]
    suitable_parts = suitable_parts.sort_values(by='price', ascending=False)
    
    if len(suitable_parts) > 0:
        recommended_part = suitable_parts.iloc[0]
        return recommended_part
    else:
        return None

def show_recommendation():
    budget, size, airflow, noise = get_user_input()
    
    recommended_part = recommend_parts(budget, size, airflow, noise)
    
    if recommended_part is not None:
        st.subheader("추천 부품:")
        st.write(f"이름: {recommended_part['name']}")
        st.write(f"가격: ${recommended_part['price']:.2f}")
        st.write(f"크기: {recommended_part['size']}mm")
        st.write(f"공기 흐름: {recommended_part['airflow']} CFM")
        st.write(f"소음 수준: {recommended_part['noise_level']} dBA")
    else:
        st.write("죄송합니다. 해당 조건에 맞는 부품을 찾을 수 없습니다.")