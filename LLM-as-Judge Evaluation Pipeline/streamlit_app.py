import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="LLM-as-Judge",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ LLM-as-Judge Evaluation Pipeline")

evaluation_type = st.sidebar.selectbox(
    "Evaluation Type",
    [
        "Pointwise",
        "Pairwise"
    ]
)

question = st.text_area("Question")

if evaluation_type == "Pointwise":

    answer = st.text_area("Candidate Answer")

    if st.button("Evaluate"):

        payload = {
            "question": question,
            "answer": answer
        }

        response = requests.post(
            f"{API_URL}/evaluate",
            json=payload
        )

        if response.status_code == 200:
            st.success("Evaluation Completed")
            st.json(response.json())
        else:
            st.error(response.text)

else:

    answer_a = st.text_area("Answer A")

    answer_b = st.text_area("Answer B")

    if st.button("Compare"):

        payload = {
            "question": question,
            "candidate_a": answer_a,
            "candidate_b": answer_b
        }

        response = requests.post(
            f"{API_URL}/pairwise",
            json=payload
        )

        if response.status_code == 200:
            st.success("Comparison Completed")
            st.json(response.json())
        else:
            st.error(response.text)