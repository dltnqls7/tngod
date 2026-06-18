import streamlit as st
import pandas as pd

st.title("👷 고용률 변화 분석")

df = pd.read_excel("고용률.xlsx", header=None)

years = pd.to_numeric(df.iloc[2, 2:], errors="coerce")

employment = pd.to_numeric(
    df.iloc[3, 2:],
    errors="coerce"
)

data = pd.DataFrame({
    "연도": years,
    "고용률": employment
}).dropna()

data["연도"] = data["연도"].astype(int)

st.subheader("연도별 고용률")

st.dataframe(data, use_container_width=True)

st.line_chart(
    data.set_index("연도")
)

change = (
    data["고용률"].iloc[-1]
    - data["고용률"].iloc[0]
)

st.metric(
    "고용률 증가",
    f"{change:.1f}%p"
)

st.markdown("""
### 분석 결과

- 고용률은 장기적으로 완만하게 상승하였다.
- 2000년 58.5%에서 2025년 62.9%까지 증가하였다.
- 단기적인 변동은 있었지만 전체적으로 증가 추세를 보였다.
""")
