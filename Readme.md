# AI-Powered SQL Query Rewriter

Transform natural language into powerful SQL queries — and understand them too — using Google Gemini + Django.

![Project Banner](https://img.shields.io/badge/Built%20With-Django%20%7C%20Gemini%20API%20%7C%20JavaScript-blue.svg)

---

###  Features

Convert plain English to SQL
Choose between SQL dialects: `MySQL`, `PostgreSQL`, `SQLite`, `Oracle`
Switch Gemini models: `gemini-2.0-flash` or `gemini-1.5-pro`
Explain any SQL query in plain English
View recent and full query history
Clean, responsive UI built with Django Templates

---

### Demo

> 📹[demo](demo/demo.gif)


### Project Structure

```bash
query_writer/
├── core/              # Django app
│   ├── views.py       # Main views and logic
│   ├── models.py      # Query history model
│   ├── urls.py
│   └── templates/
│       ├── index.html
│       └── history.html
├── api/
│   └── gemini.py      # Gemini API integration
├── .env               # API key
├── requirements.txt
└── README.md
```

---

### How It Works

1. User provides a **plain English explanation**
2. Gemini API converts it to SQL
3. The SQL is shown + explained back using another Gemini call
4. You can also speak the input instead of typing!
5. Queries are saved with timestamp, model, and dialect

---

###  Technologies Used

| Backend | Frontend | AI/LLM                       |
| ------- | -------- | ---------------------------- |
| Django  | HTML, JS | Gemini (via Google PaLM API) |

---

###  Setup Instructions

#### 1. Clone the repo

```bash
git clone https://github.com/yourusername/query-writer.git
cd query-writer
```

#### 2. Create virtual environment

```bash
python -m venv my_env
source my_env/Scripts/activate  # or source my_env/bin/activate (Linux/Mac)
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Add your Gemini API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_google_gemini_api_key
```

> You can get a free Gemini API key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

#### 5. Run the server

```bash
python manage.py migrate
python manage.py runserver
```

---

### Sample Prompts

| Explanation                           | SQL Output                                                   |
| ------------------------------------- | ------------------------------------------------------------ |
| Show all users older than 30 in India | `SELECT * FROM users WHERE age > 30 AND country = 'India';`  |
| Total sales by category               | `SELECT category, SUM(sales) FROM orders GROUP BY category;` |

---



