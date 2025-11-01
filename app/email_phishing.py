import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Email Phishing Predictor", layout="centered")
st.title("📧 Email Phishing Detection App")
st.write("Enter email feature values or upload a CSV to predict phishing emails.")


try:
    model_data = joblib.load("email_phishing_lr.pkl")  # adjust path if needed
    if len(model_data) == 3:
        model, scaler, saved_cols = model_data
        use_scaler = True
    else:
        model, saved_cols = model_data
        use_scaler = False
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.subheader("Manual Input")
input_dict = {}
for col in saved_cols:
    input_dict[col] = st.number_input(col, value=0)

if st.button("Predict Single Email"):
    input_df = pd.DataFrame([input_dict])
    if use_scaler:
        input_df = pd.DataFrame(scaler.transform(input_df), columns=saved_cols)
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1] if use_scaler else None
    if pred == 1:
        st.error(f"⚠️ This email is likely phishing. Probability: {prob:.2f}" if prob else "⚠️ This email is likely phishing.")
    else:
        st.success(f"✅ This email is likely safe. Probability: {prob:.2f}" if prob else "✅ This email is likely safe.")
