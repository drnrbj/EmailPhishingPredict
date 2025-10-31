import streamlit as st

st.set_page_config(page_title="Email Phishing Detector", layout="centered", page_icon="📧")

st.title("📧 Email Phishing Detection Demo")
st.markdown("Enter the email’s analyzed features below to predict whether it's phishing or safe:")

num_words = st.number_input("Number of Words", min_value=0)
num_unique_words = st.number_input("Unique Words", min_value=0)
num_stopwords = st.number_input("Stopwords Count", min_value=0)
num_links = st.number_input("Number of Links", min_value=0)
num_unique_domains = st.number_input("Unique Domains", min_value=0)
num_email_addresses = st.number_input("Email Addresses Count", min_value=0)
num_spelling_errors = st.number_input("Spelling Errors", min_value=0)
num_urgent_keywords = st.number_input("Urgent Keywords", min_value=0)

if st.button("Predict"):
    st.markdown("⚙️ Running prediction model...")
    st.success("✅ This email seems SAFE.") 
