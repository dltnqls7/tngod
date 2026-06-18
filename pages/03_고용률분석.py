import streamlit as st
import pandas as pd

st.title("👷 고용률 분석")

df = pd.read_excel("고용률.xlsx", header=None)

years = df.iloc[1,2:].astype(int)
employment = df.iloc[2,2:].astype(float)

data = pd.DataFrame({
    "연도": years,
    "고용률": employment
})

st.dataframe(data)

st.line_chart(
    data.set_index("연도")
)

change = employment.iloc[-1] - employment.iloc[0]

st.metric(
    "고용률 변화",
    f"{change:.1f}%p"
)
