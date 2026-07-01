# 🤖 Multi-Agent AI System

A Multi-Agent AI application built using **LangGraph**, **LangChain**, and **Groq Llama 3.3**. This project demonstrates how multiple AI agents can collaborate to solve user queries by dividing tasks among specialized agents.

---

# 🚀 Features

- 🤖 Multi-Agent Architecture
- 🔍 Research Agent
- 💻 Coding Agent
- 🧠 LangGraph Workflow
- ⚡ Groq Llama 3.3 Integration
- 💬 Interactive CLI
- 🔒 Secure API Key Management

---

# 🛠️ Tech Stack

- Python
- LangGraph
- LangChain
- Groq API
- Python Dotenv

---

# 📂 Project Structure

```text
29-Multi-Agent-AI-System/
│
├── app.py
├── agents.py
├── graph.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/adilali48/AI-Portfolio.git
```

## 2. Navigate to Project

```bash
cd 29-Multi-Agent-AI-System
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶️ Run the Project

```bash
python app.py
```

---

# 🔄 Workflow

```text
               User
                 │
                 ▼
          Multi-Agent Graph
                 │
        ┌────────┴────────┐
        ▼                 ▼
 Research Agent     Coding Agent
        │                 │
        └────────┬────────┘
                 ▼
          Final Response
```

---

# 💬 Example

### User

```text
Explain Python Lists
```

### Output

```text
🔍 Research Agent

Python Lists are ordered, mutable collections...

------------------------------------------------

💻 Coding Agent

numbers = [10,20,30]

print(numbers)
```

---

# 📦 Required Packages

- langgraph
- langchain
- langchain-groq
- python-dotenv

---

# 🎯 Learning Outcomes

This project demonstrates:

- Multi-Agent Systems
- LangGraph Workflow
- AI Orchestration
- Prompt Engineering
- Groq Integration
- Agent Collaboration
- State Management
- Graph-based AI Applications

---

# 🚀 Future Improvements

- 🧠 Supervisor Agent
- 🌐 Web Search Agent
- 📝 Writer Agent
- 📄 PDF Agent
- 🖥️ Streamlit Interface
- 🎙️ Voice-enabled Agents
- 📊 Visualization Dashboard
- Memory Support

---

# 👨‍💻 Author

**Adil Ali**

- GitHub: https://github.com/adilali48
- LinkedIn: https://linkedin.com/in/adil-ali-a28989285

---

# ⭐ Support

If you found this project helpful, give it a ⭐ on GitHub.

Happy Coding! 🚀