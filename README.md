# Super Investing AI Research Agent

An AI research agent built for the Super Investing AI Innovator Assignment – Part B.

The agent takes an NSE ticker and a set of research documents and generates a concise, evidence-based research brief in Markdown.

For the required test case, the agent analyzes:

**Sarvottam Cables Ltd (NSE: SRVCABLE)**

Sarvottam Cables Ltd is fictional for this assignment. The agent uses only the provided research documents and does not search for the company online.

## Features

- Reads company documents from `research_pack/`
- Uses an LLM through the Groq API
- Generates a concise research brief
- Includes Snapshot, Bull case, Bear case, Open questions and Sources
- Adds source citations such as `[DOC-1]`
- Identifies conflicting information between documents
- Avoids unsupported claims
- Does not provide a direct buy, sell or hold recommendation
- Saves the generated report to `output.md`

## Project Structure

```text
Super-Investing-AI-Innovator-Part-B/
│
├── agent.py
├── system_prompt.txt
├── requirements.txt
├── output.md
├── README.md
├── .gitignore
│
└── research_pack/
    ├── businessdaily_2026-08-09.md
    ├── ir_concall_2026-08-11.md
    ├── ir_press_release_2026-08-08.md
    ├── marketwatchindia_2024-03-18.md
    ├── multibaggeralerts_2026-08-12.md
    ├── nagpurcitytimes_2026-08-20.md
    ├── nse_announcement_2026-09-02.md
    └── nse_shareholding_2026-07-15.md

How to Run
1. Clone the repository
git clone https://github.com/Zafilkhan/Super-Investing-AI-Innovator-Part-B.git

2. Go to the project folder
cd Super-Investing-AI-Innovator-Part-B

3. Create a virtual environment
python -m venv .venv

4. Activate the virtual environment
Windows:
.venv\Scripts\activate

5. Install the required packages
pip install -r requirements.txt

6. Create the .env file
Create a file named .env in the project root.
Add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

Replace your_groq_api_key_here with your actual Groq API key.
The .env file should not be committed to GitHub.
7. Run the agent
python agent.py

The terminal will show the progress of the agent.
The generated research brief will be saved automatically as:
output.md

The generated brief will also be printed in the terminal.
Model Used
The project uses:
openai/gpt-oss-20b

through the Groq API.
The model was selected because it provides fast responses and is suitable for following structured research instructions and source-citation requirements.
How the Agent Works
The agent follows a simple pipeline:
Research Pack
     ↓
Load Documents
     ↓
Build Research Context
     ↓
System Prompt + Research Documents
     ↓
Groq LLM
     ↓
Research Brief
     ↓
output.md

The documents inside research_pack/ are loaded by agent.py.
The system prompt defines how the model should analyze the documents.
The research documents and instructions are then sent to the Groq-hosted model.
The model generates the final research brief, which is saved in output.md.
Research Brief Format
The generated report contains five sections:
Snapshot
Bull case
Bear case
Open questions
Sources

The output is designed for a retail investor and is kept approximately one page long.
Source Citations
The agent uses the document IDs provided in the research pack.
Examples:
[DOC-1]
[DOC-2]
[DOC-3]

Every factual claim is instructed to include a source citation.
Example:
The order book stood at ₹3,900 crore as of 30 June 2026. [DOC-3]

When multiple documents support a claim:
Management maintained FY27 revenue-growth guidance of 15–17%. [DOC-2][DOC-3]

When documents contain conflicting information, the agent reports the conflict instead of silently choosing one source.
Example:
Q1 FY27 revenue is reported as ₹1,428 crore by one source and ₹1,248 crore by another. [DOC-1][DOC-3]

Source-Only Approach
For the required SRVCABLE test case, the agent does not use internet search.
The research pack is treated as the complete source of information.
The system prompt instructs the model to:
- Use only the provided documents
- Avoid outside knowledge
- Avoid assumptions
- Avoid inventing facts
- Cite factual claims
- Identify conflicting information
- Mention missing information
- Avoid direct investment recommendations
Testing
The agent was tested at least three times as required by the assignment.
Run 1
The initial version generated the research brief, but the prompt needed stronger instructions for citation and conflict handling.
Run 2
The system prompt was improved to explicitly require source citations and to identify conflicting information between documents.
Run 3
The prompt was further improved with a final quality checklist.
The checklist verifies that:
- Snapshot is complete
- Bull case contains multiple points
- Bear case contains multiple points
- Open questions are included
- Sources are listed
- Factual claims have citations
- Conflicting information is reported
- Unsupported claims are avoided
- No outside information is used
- No buy/sell recommendation is given
- The response is concise
The final generated output is available in output.md.
Design Decision
The main design decision was to make the agent source-focused.
Instead of allowing the model to use general knowledge about a company or the stock market, the system prompt explicitly treats the provided research pack as the source of truth.
Another important decision was how to handle conflicting information.
If two documents contain different numbers, the agent does not try to decide which number is correct. It reports both figures and highlights the discrepancy under Open questions.
This helps make the research brief more transparent for a retail investor.
Limitations
The current version does not use live web search or live NSE market data.
This is intentional for the required test case because Sarvottam Cables Ltd is fictional and the assignment asks the agent to work with the provided research pack.
The current implementation also does not use a vector database or semantic retrieval.
Since the test case contains only eight documents, the documents are passed directly to the model as context.
For a larger research system, the agent could be extended with:
- Document chunking
- Embeddings
- Vector database
- RAG-based retrieval
- Live NSE data
- News search
- Support for multiple tickers
- More advanced agent tools
Security
The Groq API key is stored in the local .env file.
The .env file should never be uploaded to GitHub.
The .gitignore file excludes sensitive and unnecessary files such as:
.env
.venv/
__pycache__/

Assignment Deliverables
The repository contains the main files required for the assignment:
- agent.py — Main AI research agent
- system_prompt.txt — System prompt used by the agent
- requirements.txt — Required Python packages
- research_pack/ — Provided research documents
- output.md — Generated SRVCABLE research brief
- README.md — Project documentation
- .gitignore — Git ignore configuration
The three-run test log and 2–3 minute screen recording are submitted separately as required by the assignment.
Repository
GitHub Repository:
https://github.com/Zafilkhan/Super-Investing-AI-Innovator-Part-B
