import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_summary(rows):
    # Convert rows to a simple text summary for the AI to analyze
    data_text = ""
    for row in rows:
        data_text += (
            f"{row['Month']} | {row['Salesperson']} | {row['Region']} | "
            f"{row['Product']} | Units: {row['Units Sold']} | "
            f"Revenue: ${row['Revenue ($)']} | Achievement: {row['Achievement (%)']}%\n"
        )

    # Send data to Groq and ask for an executive summary
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": (
                f"You are a business analyst. Analyze this sales data and write "
                f"a concise 3-bullet executive summary for a CEO:\n\n{data_text}"
            )
        }]
    )

    # Extract and return the text response
    return response.choices[0].message.content


# ─── Test block ───────────────────────────────────────────
if __name__ == "__main__":
    from data.excel_reader import read_excel

    headers, rows = read_excel("data/sales_report_dummy.xlsx")
    summary = generate_summary(rows)

    print("AI Summary:\n")
    print(summary)