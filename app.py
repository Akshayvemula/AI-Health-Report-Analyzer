import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key
load_dotenv()

# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Page settings
st.set_page_config(
    page_title="AI Health Report Analyzer",
    page_icon="🩺",
    layout="centered"
)

# Title
st.title("🩺 AI Health Report Analyzer")
st.write(
    "Upload your blood report text file and receive an AI-generated health summary and Indian diet plan."
)

# Upload file
uploaded_file = st.file_uploader(
    "📄 Upload Blood Report (.txt)",
    type=["txt"]
)

if uploaded_file is not None:

    blood_work = uploaded_file.read().decode("utf-8")

    with st.expander("📄 View Blood Report"):
        st.text(blood_work)

    with st.spinner("Analyzing report..."):

        # ===================== STAGE 1 =====================
        extraction_prompt = f"""
You are a medical data extraction assistant.

From the blood report below, extract ALL test values and classify each one as HIGH, LOW, or NORMAL based on the reference ranges.

Format:

Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:

{blood_work}
"""

        extraction_response = llm.invoke(extraction_prompt)
        extracted_values = extraction_response.content

        # ===================== STAGE 2 =====================
        diet_prompt = f"""
You are a clinical nutritionist specializing in Indian dietary habits.

Give the response in EXACTLY this format:

HEALTH SUMMARY:
Write only 3 simple lines explaining the patient's condition.

DIET PLAN:

Foods to Avoid:
- item 1
- item 2
- item 3

Foods to Eat More Of:
- item 1
- item 2
- item 3

Blood Work Analysis:

{extracted_values}
"""

        diet_response = llm.invoke(diet_prompt)

    response = diet_response.content

    # Split health summary and diet plan
    if "DIET PLAN:" in response:
        health_summary = response.split("DIET PLAN:")[0]
        diet_plan = response.split("DIET PLAN:")[1]
    else:
        health_summary = response
        diet_plan = ""

    # ===================== UI =====================

    st.subheader("📋 Health Summary")
    st.info(health_summary)

    st.subheader("🥗 Suggested Diet Plan")
    st.success(diet_plan)

    with st.expander("🧪 View Extracted Lab Values"):
        st.text(extracted_values)