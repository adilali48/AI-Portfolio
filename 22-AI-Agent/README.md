# 🤖 AI Agent

A simple AI Agent built using **LangChain** and **Google Gemini**. This project demonstrates how to create an intelligent assistant capable of answering general questions while also using custom tools such as a calculator and date/time utilities.

---

## 🚀 Features

- 🤖 AI-powered conversations using Google Gemini
- 🧮 Built-in Calculator Tool
- 📅 Current Date Tool
- ⏰ Current Time Tool
- 🧩 Modular project structure
- ⚡ Fast and lightweight
- 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- LangChain
- Google Gemini API
- LangChain Core Tools
- Python Dotenv

---

## 📂 Project Structure

```text
22-AI-Agent/
│
├── app.py
├── agent.py
├── tools.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/adilali48/AI-Portfolio.git
```

### 2. Navigate to the Project

```bash
cd 22-AI-Agent
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💬 Example Usage

### Ask AI Questions

```text
What is Artificial Intelligence?
```

```text
Explain LangChain
```

```text
What is RAG?
```

---

### Calculator Tool

```text
calc: 25*8
```

Output

```text
200
```

---

### Date Tool

```text
What is today's date?
```

Output

```text
30 June 2026
```

---

### Time Tool

```text
What time is it?
```

Output

```text
07:30 PM
```

---

## 🧠 Architecture

```text
            User
              │
              ▼
         AI Agent (app.py)
              │
      ┌───────┴────────┐
      │                │
      ▼                ▼
 Gemini LLM        Custom Tools
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     Calculator     Date        Time
```

---

## 📦 Required Packages

- langchain
- langchain-core
- langchain-google-genai
- python-dotenv

---

## 🎯 Learning Outcomes

This project demonstrates:

- AI Agent Fundamentals
- Google Gemini Integration
- LangChain Basics
- Custom Tool Development
- Modular Project Design
- Environment Variable Management
- AI-Powered Command Line Applications

---

## 🚀 Future Improvements

- 🌐 Web Search Tool
- 📂 File Reader Tool
- 💬 Conversation Memory
- 🎙️ Voice Assistant
- 🖥️ Streamlit Web Interface
- 🔍 Tool Calling Agent
- 🧠 LangGraph Integration

---

## 👨‍💻 Author

**Adil Ali**

- 🐙 GitHub: https://github.com/adilali48
- 💼 LinkedIn: https://linkedin.com/in/adil-ali-a28989285

---

## ⭐ Support

If you found this project helpful, consider giving the repository a ⭐ on GitHub.

Happy Coding! 🚀