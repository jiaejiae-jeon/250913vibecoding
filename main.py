import streamlit as st
import pandas as pd
import altair as alt
import os

st.set_page_config(page_title="MBTI Country Analysis", layout="wide")

st.title("🌍 MBTI 유형별 국가 TOP 10")
st.write("CSV 데이터를 기반으로 MBTI 유형별 비율이 가장 높은 국가 TOP 10을 시각화합니다.")

# 기본 파일 경로
default_file = "countriesMBTI_16types.csv"

# 데이터 불러오기
if os.path.exists(default_file):
    df = pd.read_csv(default_file)
    st.success(f"기본 데이터 파일을 불러왔습니다: {default_file}")
else:
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("업로드한 파일을 불러왔습니다.")
    else:
        st.error("CSV 파일이 필요합니다. 기본 파일이 없으니 업로드해주세요.")
        st.stop()

# MBTI 유형 리스트 (첫 열은 Country라 제외)
mbti_types = df.columns[1:].tolist()

# 사용자 선택
selected_type = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

# 선택한 MBTI 기준 TOP10 추출
top10 = df[["Country", selected_type]].nlargest(10, selected_type)

st.subheader(f"🌟 {selected_type} 비율이 가장 높은 국가 TOP 10")

# Altair 그래프
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(selected_type, title=f"{selected_type} 비율"),
        y=alt.Y("Country", sort="-x"),
        tooltip=["Country", selected_type]
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)

# 데이터 테이블 표시
st.dataframe(top10.set_index("Country"))
