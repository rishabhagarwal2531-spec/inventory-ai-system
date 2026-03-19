from demand_forecast import run_forecast
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.text import MIMEText


# CONNECT
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1MdqUU-mld319Pq_2BF3XBcTloc2usIVMtbMcw7bio-A")

sales_sheet = sheet.worksheet("sales_log")
inventory_sheet = sheet.worksheet("inventory")

sales = pd.DataFrame(sales_sheet.get_all_records())
inventory = pd.DataFrame(inventory_sheet.get_all_records())
results_df = run_forecast(client)
results_df.to_csv("inventory_decisions.csv", index=False)
print("📊 CSV updated for Power BI")
print(results_df)

# CLEAN
sales['date'] = pd.to_datetime(sales['date'])


# -------- EMAIL SECTION --------
sender = "rishabhagarwal2531@gmail.com"
receiver = "rishabhagarwal2531@gmail.com"
password = "utwjadyllgjwxfjj"
summary_text = "📦 INVENTORY DECISION REPORT\n\n"

for index, row in results_df.iterrows():
    summary_text += f"""
Product: {row['product']}
Stock: {row['current_stock']}
Avg Demand: {row['avg_daily_demand']}
Days Left: {row['days_left']}
Status: {row['status']}
Recommended Order: {row['recommended_order_qty']}
-----------------------------
"""

msg = MIMEText(summary_text)
msg["Subject"] = "Daily Inventory Decision Report"
msg["From"] = sender
msg["To"] = receiver

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()

print("\nEmail sent successfully!")
print(results_df.columns)





