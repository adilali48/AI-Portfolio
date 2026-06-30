# 🤖 AI SQL Database Agent

An AI-powered SQL Database Assistant built with **Python**, **SQLite**, and **Google Gemini**. This application allows users to ask questions in plain English, automatically converts them into SQL queries, executes the queries on a SQLite database, and returns the results.

---

## 🚀 Features

- 🤖 Natural Language to SQL
- 🗄️ SQLite Database Integration
- 🧠 Google Gemini AI
- ⚡ Automatic SQL Generation
- 📊 Query Execution
- 🔒 Secure API Key Management
- 🧩 Modular Project Structure

---

## 🛠️ Tech Stack

- Python
- SQLite
- Google Gemini API
- LangChain
- Python Dotenv

---

## 📂 Project Structure

```text
25-AI-SQL-Agent/
│
├── app.py
├── agent.py
├── database.py
├── sample.db
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
cd 25-AI-SQL-Agent
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Create the Database

Run:

```bash
python database.py
```

This creates the SQLite database (`sample.db`) and inserts sample employee records.

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 💬 Example Questions

```text
Show all employees
```

```text
Show IT employees
```

```text
Who has the highest salary?
```

```text
How many employees are there?
```

```text
Show employees whose salary is greater than 70000
```

---

## 🧠 How It Works

```text
User Question
      │
      ▼
Google Gemini
      │
      ▼
Generate SQL Query
      │
      ▼
SQLite Database
      │
      ▼
Execute SQL
      │
      ▼
Display Results
```

---

## 📦 Required Packages

- langchain
- langchain-google-genai
- python-dotenv
- sqlite3 (built into Python)

---

## 🎯 Learning Outcomes

This project demonstrates:

- Natural Language Processing (NLP)
- AI-powered SQL Generation
- SQLite Database Operations
- Prompt Engineering
- Python Database Programming
- LangChain Integration

---

## 🚀 Future Improvements

- 🌐 Streamlit Web Interface
- 📊 Database Visualization
- 📝 SQL Query History
- 📁 Support Multiple Tables
- 📈 Charts and Graphs
- 🔐 User Authentication
- ☁️ Cloud Database Support (MySQL/PostgreSQL)

---

## 👨‍💻 Author

**Adil Ali**

- 🐙 GitHub: https://github.com/adilali48
- 💼 LinkedIn: https://linkedin.com/in/adil-ali-a28989285

---

## ⭐ Support

If you found this project useful, please give the repository a ⭐.

Happy Coding! 🚀