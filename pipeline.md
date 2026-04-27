Data Flow

Zapier Trigger → API → Python → Google Sheets → Gmail

ETL 對應
Extract：Alpha Vantage API
Transform：Python 處理價格判斷
Load：Google Sheets
Event-driven

當價格 < threshold 時觸發通知

Error Handling
API failure retry
Missing data handling
Future Upgrade
Kafka streaming
Airflow orchestration
