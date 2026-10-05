# Super Investing AI Research Agent

AI research agent built for the **Super Investing AI Innovator Assignment – Part B**.

The agent analyzes **Sarvottam Cables Ltd (NSE: SRVCABLE)** using the provided research documents and generates a concise research brief.

## Features

- Reads documents from `research_pack/`
- Uses Groq API
- Generates an investor research brief
- Includes Snapshot, Bull case, Bear case, Open questions and Sources
- Adds source citations such as `[DOC-1]`
- Identifies conflicting information
- Saves the result to `output.md`

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
cd Super-Investing-AI-Innovator-Part-B

2. Create a virtual environment
python -m venv .venv

3. Activate the environment
Windows:
.venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Add Groq API key
Create a .env file in the project folder:
GROQ_API_KEY=your_groq_api_key_here

6. Run the agent
python agent.py

The generated research brief will be saved in:
output.md

Model
The agent uses openai/gpt-oss-20b through the Groq API.
It was selected for fast generation and good instruction following.
How It Works
Research Pack
     ↓
Load Documents
     ↓
System Prompt + Documents
     ↓
Groq LLM
     ↓
Research Brief
     ↓
output.md

The agent uses only the documents provided in research_pack/.


Output
The generated brief contains:
- Snapshot
- Bull case
- Bear case
- Open questions
- Sources
Factual claims are supported using document citations such as:
The order book stood at ₹3,900 crore. [DOC-3]

Conflicting information is reported instead of being silently resolved.
Testing
The agent was tested three times with improvements to the prompt.
- Run 1: Basic research brief generation.
- Run 2: Improved citation and conflict handling.
- Run 3: Added a final quality checklist to improve completeness.
The final output is available in output.md.
Design Decision
The agent follows a source-first approach.
It uses the provided research documents as the only source of information and does not use outside knowledge for the SRVCABLE test case.
When sources contain conflicting information, the agent reports the conflict under Open questions.
Limitations
- The current version is focused on the provided SRVCABLE research pack.
- Live market and NSE data are not included.
Repository
GitHub:
https://github.com/Zafilkhan/Super-Investing-AI-Innovator-Part-B
