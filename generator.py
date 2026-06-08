from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import pdfkit

# Path to wkhtmltopdf executable on Windows
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

def build_report(headers, rows, ai_summary):
    # Set up Jinja2 to load templates from the templates folder
    env = Environment(loader=FileSystemLoader("report/templates"))
    template = env.get_template("report.html")

    # Fill in the template with actual data
    html_content = template.render(
        report_title="Monthly Sales Report",
        date=datetime.now().strftime("%B %d, %Y"),
        total_records=len(rows),
        headers=headers,
        rows=rows,
        ai_summary=ai_summary
    )

    # Save rendered HTML temporarily
    os.makedirs("output", exist_ok=True)
    html_path = "output/report_temp.html"
    pdf_path = "output/report.pdf"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Convert HTML to PDF using wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    pdfkit.from_file(html_path, pdf_path, configuration=config)

    # Remove temp HTML file
    os.remove(html_path)

    print(f"✅ PDF report saved to {pdf_path}")
    return pdf_path


# ─── Test block ───────────────────────────────────────────
if __name__ == "__main__":
    from data.excel_reader import read_excel
    from report.ai_summary import generate_summary

    headers, rows = read_excel("data/sales_report_dummy.xlsx")
    summary = generate_summary(rows)
    path = build_report(headers, rows, summary)

    print("Done! Open", path, "to preview the PDF.")