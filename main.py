import schedule
import time
from data.excel_reader import read_excel
from report.ai_summary import generate_summary
from report.generator import build_report
from email_sender import send_report

def run_report():
    print("Starting report generation...")

    # Step 1: Read data from Excel
    headers, rows = read_excel("data/sales_report_dummy.xlsx")
    print(f"-Data loaded — {len(rows)} rows")

    # Step 2: Generate AI summary
    summary = generate_summary(rows)
    print("- AI summary generated")

    # Step 3: Build PDF report
    pdf_path = build_report(headers, rows, summary)
    print("- PDF report created")

    # Step 4: Email the report
    send_report(pdf_path)
    print("- Report emailed successfully")

    print(" All done!\n")


# ─── Schedule Configuration ───────────────────────────────

# Run every Monday at 8:00 AM
schedule.every().monday.at("08:00").do(run_report)

# Other options (uncomment as needed):
# schedule.every().day.at("08:00").do(run_report)       # daily
# schedule.every().month.do(run_report)                  # monthly
# schedule.every(10).minutes.do(run_report)              # every 10 mins (for testing)


# ─── Test: run immediately once ───────────────────────────
if __name__ == "__main__":
    print(" Report Generator started. Running once now for test...\n")
    run_report()

    print(" Scheduler running. Waiting for next scheduled run...")
    print("   Press Ctrl+C to stop.\n")

    # Keep the script running so schedule can trigger future runs
    while True:
        schedule.run_pending()
        time.sleep(60)
