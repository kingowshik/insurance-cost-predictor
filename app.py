import streamlit as st
import pickle
import numpy as np

# page config
st.set_page_config(
    page_title="Insurance Predictor",
    page_icon="💰",
    layout="centered"
)

# load model
model = pickle.load(open("insurance_model.pkl", "rb"))

# title
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>💰 Insurance Cost Predictor</h1>", unsafe_allow_html=True)

st.markdown("---")

st.write("### Enter your details:")

# columns layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🎂 Age", 18, 100, 25)
    bmi = st.number_input("⚖️ BMI", 10.0, 50.0, 25.0)
    children = st.number_input("👶 Children", 0, 5, 0)

with col2:
    sex = st.selectbox("🧑 Sex", ["male", "female"])
    smoker = st.selectbox("🚬 Smoker", ["yes", "no"])
    region = st.selectbox("🌍 Region", ["northwest", "southeast", "southwest", "northeast"])


# encoding
sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0


input_data = np.array([[
    age,
    bmi,
    children,
    sex_male,
    smoker_yes,
    region_northwest,
    region_southeast,
    region_southwest
]])


# predict button
if st.button("🔮 Predict Insurance Cost", use_container_width=True):

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    st.success(f"💵 Estimated Insurance Cost: **{prediction:,.2f}**")

    if prediction < 10000:
        st.info("✅ Low insurance cost")

    elif prediction < 30000:
        st.warning("⚠️ Moderate insurance cost")

    else:
        st.error("🚨 High insurance cost")


st.markdown("---")

st.caption("Built with ❤️ using Streamlit and Machine Learning")