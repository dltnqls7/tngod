import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 상관관계 분석 및 결론")

# 최저임금
w = pd.read_excel("최저임금.xlsx", header=None)

years = pd.to_numeric(w.iloc[2,1:], errors="coerce")

wage = (
    w.iloc[3,1:]
    .astype(str)
    .str.replace(",", "", regex=False)
)

wage = pd.to_numeric(wage, errors="coerce")

# 고용률
e = pd.read_excel("고용률.xlsx", header=None)

employment = pd.to_numeric(
    e.iloc[3,2:],
    errors="coerce"
)

data = pd.DataFrame({
    "연도": years,
    "최저임금": wage,
    "고용률": employment
}).dropna()

data["연도"] = data["연도"].astype(int)

corr = data["최저임금"].corr(data["고용률"])

st.metric(
    "상관계수(Pearson)",
    f"{corr:.3f}"
)

st.subheader("산점도")

fig, ax = plt.subplots(figsize=(6,4))

ax.scatter(
    data["최저임금"],
    data["고용률"]
)

ax.set_xlabel("최저임금")
ax.set_ylabel("고용률")

st.pyplot(fig)

st.subheader("분석 결과")

st.write(f"""
상관계수는 **{corr:.3f}**으로 나타났다.

이는 두 변수 사이에 양의 상관관계가 있음을 의미한다.

즉, 최저임금이 상승한 기간 동안 고용률도 함께 증가하는 경향이 관찰되었다.

그러나 상관관계는 인과관계를 의미하지 않는다.

경제성장률, 물가상승률, 산업구조 변화, 정부 정책 등 다양한 요인이 고용률에 영향을 미칠 수 있으므로 최저임금만으로 고용률의 변화를 설명할 수는 없다.
""")

st.info("""
### 프로젝트 결론

• 최저임금은 지속적으로 상승하였다.

• 고용률도 장기적으로 증가하였다.

• 두 변수는 양의 상관관계를 보였다.

• 최저임금 인상이 반드시 고용 감소를 초래한다고 결론 내릴 수는 없었다.
""")
