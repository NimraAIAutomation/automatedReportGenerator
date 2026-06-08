#  Automated Report Generator

> Pull data from Excel → Generate AI-summarized PDF report → Email it automatically on a schedule.

Built for executives who need insights delivered to their inbox - not spreadsheets to dig through.

---

##  What It Does

- Reads sales data from an Excel file automatically
- Generates an AI-powered executive summary using Groq API
- Converts the report into a clean, formatted PDF
- Emails the PDF to any recipient on a schedule (daily/weekly/monthly)
- Fully automated — zero manual work after setup

---

## Tech Stack

| Layer | Tool |
|---|---|
| Data Source | Excel (.xlsx) via `openpyxl` |
| AI Summary | Groq API (LLaMA 3.3) |
| Report Template | Jinja2 (HTML) |
| PDF Generation | pdfkit + wkhtmltopdf |
| Email Delivery | smtplib (Gmail SMTP) |
| Scheduling | `schedule` library |
| Config | `.env` + `python-dotenv` |

---

##  Setup

### 1. Clone the repo
```bash
git clone https://github.com/YourUsername/report-generator.git
cd report-generator
```

### 2. Create conda environment
```bash
conda create -n reportgenerator python=3.11
conda activate reportgenerator
```

### 3. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Install wkhtmltopdf (Windows)
Download and install from: https://wkhtmltopdf.org/downloads.html

Default path: `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`

### 5. Configure `.env`
Create a `.env` file in the project root:

EMAIL_ADDRESS=you@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
RECIPIENT_EMAIL=recipient@gmail.com
GROQ_API_KEY=your_groq_api_key

> **Gmail App Password:** Google Account → Security → 2-Step Verification → App Passwords

---

## Run

```bash
python main.py
```

Runs once immediately as a test, then waits for the next scheduled run (default: every Monday at 8:00 AM).

---

## Change Schedule

Edit these lines in `main.py`:

```python
schedule.every().monday.at("08:00").do(run_report)   # weekly
schedule.every().day.at("08:00").do(run_report)       # daily
schedule.every(10).minutes.do(run_report)             # every 10 mins (testing)
```

---

## Sample Output

The recipient receives a PDF email attachment containing:
- Report title and generation date
- AI executive summary (3 bullet insights)
- Full data table from Excel

---

##  Related Projects

- [Project 1 — AI Email Auto-Responder](https://github.com/NimraAIAutomation/email-auto-responder)

---

## Author

Built by **Nimra** — Python Automation Developer  
Specializing in AI-powered business automation for CEOs and executives.

