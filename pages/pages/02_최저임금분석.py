import streamlit as st
import pandas as pd

st.title("💰 최저임금 분석")

df = pd.read_excel("최저임금.xlsx", header=None)

years = df.iloc[1,1:].astype(int)
wage = (
    df.iloc[2,1:]
    .astype(str)
    .str.replace(",","")
    .astype(int)
)

data = pd.DataFrame({
    "연도": years,
    "최저임금": wage
})

st.dataframe(data)

st.line_chart(
    data.set_index("연도")
)

st.metric(
    "최저임금 증가배수",
    f"{round(wage.iloc[-1]/wage.iloc[0],2)}배"
)
