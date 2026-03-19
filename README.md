# 📦 AI Inventory Management System

An end-to-end data analytics + automation project that predicts demand, prevents stockouts, and automates inventory decisions.

---

## 🚀 Project Overview

This system combines:
- 📊 Power BI Dashboard (visual insights)
- 🤖 Python Forecasting (Prophet model)
- 📧 Email Automation (reorder alerts)
- ☁️ Google Sheets (live data source)

---

## 🧠 Key Features

- Demand forecasting using Facebook Prophet
- Automatic reorder recommendations
- Inventory health classification:
  - URGENT REORDER
  - REORDER SOON
  - OK
- Email alerts for low stock
- Power BI dashboard for visualization

---

## 🏗️ Tech Stack

- Python (Pandas, Prophet)
- Power BI
- Google Sheets API (gspread)
- SMTP (Email automation)

---

## 📊 Workflow

1. Data stored in Google Sheets  
2. Python fetches and cleans data  
3. Forecasting model predicts demand  
4. Inventory logic calculates:
   - Avg daily demand
   - Days left
   - Reorder quantity  
5. Results saved as CSV  
6. Power BI dashboard visualizes results  
7. Email alerts sent automatically  

---

## 📁 Project Structure

```
inventory_ai/
│
├── demand_forecast.py
├── inventory_engine.py
├── inventory_decisions.csv
├── credentials.json (not uploaded for security)
├── run_inventory.bat
```

---

## 📈 Sample Output

| Product | Stock | Days Left | Status | Order Qty |
|--------|------|----------|--------|----------|
| Item A | 40   | 6.7      | REORDER SOON | 41 |
| Item B | 25   | 4.2      | URGENT REORDER | 40 |

---

## 🔐 Note

Sensitive files like `credentials.json` are excluded for security.

---

## 💡 Business Impact

- Prevents stockouts
- Optimizes inventory levels
- Automates decision-making
- Reduces manual effort

---

## 👤 Author

**Rishabh Agarwal**  
Aspiring Data Analyst | Power BI | Python  

---

## ⭐ If you found this useful, give it a star!
