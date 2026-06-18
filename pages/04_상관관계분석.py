import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 상관관계 분석")

wage_df = pd.read_excel("최저임금.xlsx", header=None)
emp_df = pd.read_excel("고용률.xlsx", header=None)

years = wage_df.iloc[1,1:].astype(int)

wage = (
    wage_df.iloc[2,1:]
    .astype(str)
    .str.replace(",","")
    .astype(float)
)

emp = emp_df.iloc[2,2:].astype(float)

data = pd.DataFrame({
    "연도": years,
    "최저임금": wage,
    "고용률": emp
})

corr = data["최저임금"].corr(data["고용률"])

st.subheader("상관계수")

st.metric(
    "Pearson r",
    f"{corr:.3f}"
)

fig, ax = plt.subplots()

ax.scatter(
    data["최저임금"],
    data["고용률"]
)

ax.set_xlabel("최저임금")
ax.set_ylabel("고용률")

st.pyplot(fig)

if corr > 0.7:
    st.success("강한 양의 상관관계가 나타납니다.")
else:
    st.warning("뚜렷한 상관관계가 없습니다.")
