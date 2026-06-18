import streamlit as st
import pandas as pd

st.title("💰 최저임금 변화 분석")

# 엑셀 읽기
df = pd.read_excel("최저임금.xlsx", header=None)

# 연도 (3행)
years = pd.to_numeric(df.iloc[2, 1:], errors="coerce")

# 최저임금 (4행)
wage = (
    df.iloc[3, 1:]
    .astype(str)
    .str.replace(",", "", regex=False)
)

wage = pd.to_numeric(wage, errors="coerce")

# 데이터프레임 생성
data = pd.DataFrame({
    "연도": years,
    "최저임금": wage
}).dropna()

data["연도"] = data["연도"].astype(int)

st.subheader("연도별 최저임금")

st.dataframe(data, use_container_width=True)

st.line_chart(
    data.set_index("연도")
)

increase = data["최저임금"].iloc[-1] / data["최저임금"].iloc[0]

st.metric(
    "2000년 대비 증가",
    f"{increase:.2f}배"
)

st.markdown("""
### 분석 결과

- 최저임금은 매년 꾸준히 상승하였다.
- 2000년 1,600원에서 2025년 10,030원으로 약 6.27배 증가하였다.
- 특히 2018년에 가장 큰 폭으로 인상되었다.
""")
