import streamlit as st
from parser import parse_architecture
from parser import *
from threat_engine import analyze_architecture

st.set_page_config(
    page_title="AI Threat Modeling Assistant",
    page_icon="🛡️",
    layout="wide"
)
st.write(GROQ_API_KEY)
st.title("🛡️ AI Threat Modeling Assistant")
st.markdown(
    """
Describe your AI application's architecture. The system will identify
the architecture components (assets) and later generate a threat model.
"""
)

st.subheader("Architecture Description")

default_text = """Example:

We have a customer support chatbot built using GPT-4.

The chatbot uses Retrieval-Augmented Generation (RAG) with a Pinecone vector database.

It stores conversation history in Redis.

The agent has access to:
- Web Search
- Outlook Email API

The application is deployed on Azure.

Authentication is handled using OAuth2.

Logs are stored in Elasticsearch.
"""

architecture_description = st.text_area(
    "Describe your AI system",
    value=default_text,
    height=350,
    placeholder="Describe your AI architecture..."
)

col1, col2 = st.columns([1, 5])

with col1:
    analyze = st.button("Analyze", type="primary")

if analyze:

    if architecture_description.strip() == "":
        st.error("Please enter an architecture description.")
        st.stop()

    st.success("Architecture description received!")

    st.subheader("Input Received")

    st.code(architecture_description, language="text")
    architecture = parse_architecture(architecture_description)

    st.subheader("Extracted Architecture")

    st.json(architecture)





    threats = analyze_architecture(architecture)

    st.subheader("Detected Threats")

    for threat in threats:

        st.error(threat["name"])

        st.write("Severity:", threat["severity"])

        st.write("Reason:")

        st.info(threat["reason"])

        st.write("OWASP")

        st.json(threat["framework"]["OWASP"])

        st.write("MITRE")

        st.json(threat["framework"]["MITRE"])

        st.divider()