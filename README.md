<p align="center">
  <img src="https://img.shields.io/badge/InquiroLogic--AI-SQL%20Assistant-blueviolet?style=for-the-badge&logo=robot&logoColor=white" alt="InquiroLogic-AI"/>
</p>

<h1 align="center">🧠 InquiroLogic-AI</h1>

<p align="center">
  <strong>An Intelligent Natural Language to SQL Query Assistant</strong><br>
  <em>Powered by Groq LLM, LangChain & Streamlit</em>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#demo">Demo</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/LangChain-Framework-green?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=flat-square&logo=groq&logoColor=white" alt="Groq"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"/>
</p>

---

## 🚀 Overview

**InquiroLogic-AI** is a cutting-edge conversational AI application that transforms natural language queries into SQL commands. Simply ask questions in plain English, and watch as the AI agent intelligently interacts with your database to retrieve the information you need.

> 💡 *"Talk to your database like you talk to a colleague"*

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🗣️ **Natural Language Processing** | Ask questions in plain English - no SQL knowledge required |
| 🔗 **Multi-Database Support** | Seamlessly connect to SQLite or MySQL databases |
| ⚡ **Real-time Streaming** | Watch the AI think and respond in real-time |
| 🧩 **Intelligent SQL Agent** | Powered by LangChain's ReAct agent architecture |
| 🔒 **Secure Connections** | Read-only database access for safety |
| 💬 **Conversation History** | Maintains chat context for follow-up questions |
| 🎨 **Modern UI** | Clean, intuitive Streamlit interface |

---

## 🎬 Demo

```
User: "Show me all students who scored above 90"
AI:   Querying the database...
      → SELECT * FROM STUDENT WHERE MARKS > 90
      
      Found 2 students:
      - Michael Brown (9th Grade, Section C) - 92 marks
      - Jessica Wilson (10th Grade, Section A) - 95 marks
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.9 or higher
- Groq API Key ([Get one here](https://console.groq.com/))
- Git

### Quick Start

```bash
# Clone the repository
git clone https://github.com/anshika368/InquiroLogic-AI.git
cd InquiroLogic-AI

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize the sample database (optional)
python sqlite.py

# Launch the application
streamlit run app.py
```

---

## 📖 Usage

### 1️⃣ Start the Application
```bash
streamlit run app.py
```

### 2️⃣ Configure Database
- **SQLite (Default)**: Uses the local `student.db` file
- **MySQL**: Enter your connection details in the sidebar

### 3️⃣ Enter API Key
- Input your Groq API key in the sidebar

### 4️⃣ Start Chatting!
Ask questions like:
- *"How many students are in 10th grade?"*
- *"What's the average marks in Section A?"*
- *"List all students sorted by marks"*
- *"Who has the highest marks?"*

---

## 🏗️ Tech Stack

<table>
<tr>
<td align="center" width="150">
<img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="60"/><br>
<b>Python</b><br>
<sub>Core Language</sub>
</td>
<td align="center" width="150">
<img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="60"/><br>
<b>Streamlit</b><br>
<sub>Web Framework</sub>
</td>
<td align="center" width="150">
<img src="https://python.langchain.com/img/brand/wordmark-dark.png" width="80"/><br>
<b>LangChain</b><br>
<sub>LLM Framework</sub>
</td>
<td align="center" width="150">
<b>🚀 Groq</b><br>
<sub>LLM Provider</sub>
</td>
</tr>
</table>

### Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Interactive web application |
| `langchain` | LLM orchestration framework |
| `langchain-groq` | Groq LLM integration |
| `langchain-community` | SQL toolkit & utilities |
| `sqlalchemy` | Database abstraction layer |
| `sqlite3` | Local database support |

---

## 📁 Project Structure

```
InquiroLogic-AI/
├── 📄 app.py              # Main Streamlit application
├── 📄 sqlite.py           # Database initialization script
├── 📄 requirements.txt    # Python dependencies
├── 📄 README.md           # Project documentation
├── 🗄️ student.db          # SQLite database (auto-generated)
└── 📁 venv/               # Virtual environment
```

---

## ⚙️ Configuration

### Environment Variables (Optional)

Create a `.env` file for persistent configuration:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### MySQL Connection

To connect to a MySQL database:

1. Select "Use MySQL database" in the sidebar
2. Enter your connection details:
   - Host: `localhost` (or your server)
   - User: Your MySQL username
   - Password: Your MySQL password
   - Database: Target database name

---

## 🔐 Security Features

- ✅ **Read-only SQLite access** - Prevents accidental data modification
- ✅ **Password masking** - API keys and passwords are hidden
- ✅ **No credential storage** - Sensitive data stays in session only
- ✅ **Parsing error handling** - Graceful error recovery

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📋 Roadmap

- [ ] 🔄 Support for PostgreSQL
- [ ] 📊 Query result visualization
- [ ] 💾 Export results to CSV/Excel
- [ ] 🔐 OAuth authentication
- [ ] 📱 Mobile-responsive design
- [ ] 🌐 Multi-language support

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Anshika**

[![GitHub](https://img.shields.io/badge/GitHub-anshika368-181717?style=flat-square&logo=github)](https://github.com/anshika368)

---

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the amazing LLM framework
- [Groq](https://groq.com/) for lightning-fast LLM inference
- [Streamlit](https://streamlit.io/) for the intuitive UI framework

---

<p align="center">
  <strong>⭐ Star this repository if you found it helpful!</strong>
</p>

<p align="center">
  Made with ❤️ and 🤖
</p>
