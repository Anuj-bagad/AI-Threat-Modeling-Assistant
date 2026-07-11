import json
from openai import OpenAI

# ==========================================================
# Enter your Groq API Key here
# ==========================================================

GROQ_API_KEY = "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"

# ==========================================================
# Groq Client
# ==========================================================

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

# ==========================================================
# Model
# ==========================================================

MODEL = "llama-3.3-70b-versatile"
# You can change this to a Qwen model if Groq exposes one.
# Example:
# MODEL = "qwen/qwen3-32b"

# ==========================================================
# System Prompt
# ==========================================================

SYSTEM_PROMPT = """
You are an AI Architecture Parser.

Your job is to extract architecture components from the user's
description of an AI system.

Return ONLY valid JSON.

Rules:

1. Do NOT hallucinate.
2. Extract ONLY information explicitly mentioned.
3. If information is absent, use null or [].
4. Relationships should be inferred only when obvious.

Return JSON in this format:

{
    "nodes":[
        {
            "id":"",
            "type":"",
            "name":""
        }
    ],
    "edges":[
        {
            "source":"",
            "target":"",
            "relationship":""
        }
    ]
}

Allowed node types:

User
LLM
Agent
Retriever
VectorDB
Memory
Tool
Database
API
Authentication
Deployment
Logging
Storage
KnowledgeBase

Relationship examples:

interacts_with
uses
calls
retrieves_from
stores_to
authenticated_by
logs_to
deployed_on
"""

# ==========================================================
# Parser
# ==========================================================


def parse_architecture(description: str):

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": description
            }
        ]
    )

    output = response.choices[0].message.content

    return json.loads(output)


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    architecture_description = """
    We built a customer support chatbot.

    It uses GPT-4.

    RAG is enabled using Pinecone.

    Conversation history is stored in Redis.

    The chatbot can use:
    - Web Search
    - Outlook Email API

    Authentication is OAuth2.

    Logs are stored in Elasticsearch.

    Deployment is on Azure.
    """

    architecture = parse_architecture(architecture_description)

    print(json.dumps(architecture, indent=4))