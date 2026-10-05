import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


# Configuration

RESEARCH_PACK_DIR = Path("research_pack")
SYSTEM_PROMPT_FILE = Path("system_prompt.txt")
OUTPUT_FILE = Path("output.md")

TICKER = "SRVCABLE"

# this is not fix model we can change it anytime 
MODEL = "openai/gpt-oss-20b"



# Load system prompt
def load_system_prompt():
    if not SYSTEM_PROMPT_FILE.exists():
        raise FileNotFoundError(
            f"{SYSTEM_PROMPT_FILE} not found."
        )

    return SYSTEM_PROMPT_FILE.read_text(encoding="utf-8")



# Load research documents

def load_documents():
    if not RESEARCH_PACK_DIR.exists():
        raise FileNotFoundError(
            f"{RESEARCH_PACK_DIR} folder not found."
        )

    documents = []

    for file_path in sorted(RESEARCH_PACK_DIR.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")

        documents.append(
            f"""
==================================================
DOCUMENT: {file_path.name}
SOURCE ID: {file_path.stem}
==================================================

{content}
"""
        )

    if not documents:
        raise ValueError(
            "No .md documents found in research_pack/"
        )

    return "\n".join(documents)


# Create user prompt

def build_user_prompt(documents):
    return f"""
Research the company with NSE ticker: {TICKER}.

The following documents are the complete research pack.

IMPORTANT:
- Use ONLY these documents.
- Do not use internet knowledge.
- Do not assume facts that are not present.
- Treat the documents as the source of truth.
- If two sources disagree, do NOT silently choose one.
- Mention the disagreement in "Open questions".
- Every factual claim must have a source citation.

RESEARCH PACK:

{documents}

Generate a concise investor research brief in Markdown.

Required sections:

1. Snapshot
2. Bull case
3. Bear case
4. Open questions
5. Sources

Keep it around one page and write for a retail investor.
"""



# Generate research brief

def generate_brief(client, system_prompt, user_prompt):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.2,
        max_tokens=6000
    )

    message = response.choices[0].message

    print("\n===== MODEL RESPONSE =====")
    print("Finish reason:", response.choices[0].finish_reason)
    print("Content length:", len(message.content or ""))
    print("==========================\n")

    content = message.content

    if not content or not content.strip():
        raise ValueError(
            f"Model returned an empty response. "
            f"Finish reason: {response.choices[0].finish_reason}"
        )

    return content


# -----------------------------
# Main
# -----------------------------

def main():

    print("Starting SRVCABLE Research Agent...\n")

    #  i used the groq api key 
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found. "
            "Add it to your .env file."
        )

    # Create Groq client
    client = Groq(api_key=api_key)

    # Load system prompt
    print("Loading system prompt...")
    system_prompt = load_system_prompt()

    # Load documents
    print("Loading research documents...")
    documents = load_documents()

    print("Documents loaded successfully.\n")

    # Build prompt
    user_prompt = build_user_prompt(documents)

    # Generate answer
    print("Generating research brief...\n")

    brief = generate_brief(
        client,
        system_prompt,
        user_prompt
    )

    # Save output
    OUTPUT_FILE.write_text(
        brief,
        encoding="utf-8"
    )

    print("Research brief generated successfully!")
    print(f"Saved to: {OUTPUT_FILE}")

    print("\n" + "=" * 60)
    print(brief)
    print("=" * 60)


if __name__ == "__main__":
    main()