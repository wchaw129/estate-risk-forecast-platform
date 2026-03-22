# 📌 Housing Price Prediction & Analysis 

## 🧠 Description
This project is a tool for analyzing and predicting housing prices in Poland based on data collected via web scraping from Otodom.

## 🚧 Status
Work in Progress (WIP)

## Features
* Web scraping of apartment listings 
* Relational database (PostgreSQL)
* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Housing price prediction model
* Interactive dashboard (Power BI / Streamlit)

## 🛠️ Tech Stack
* Python
* BeautifulSoup 
* Pandas / NumPy
* SQL (PostgreSQL)
* scikit-learn
* Power BI/Streamlit

## Database Documentation
Data structure documentation for the **Estate Risk Forecast Platform**. The database is designed to store historical real estate pricing data and monitor listing activity from Otodom.

### Entity Relationship Diagram (ERD)
```mermaid
erDiagram
    LOGS ||--o{ PROPERTY : "tracks first/last seen"
    LOGS ||--o{ PRICE_HISTORY : "records change during"
    PROPERTY ||--o{ PRICE_HISTORY : "has"

    LOGS {
        INTEGER id_scan PK "Auto-increment"
        TIMESTAMP start_time "Start of the scraping session"
        TIMESTAMP end_time "End of the scraping session"
        INTEGER offers_found "Total organic listings detected"
        INTEGER new_offers "Count of brand new listings"
        INTEGER price_changes "Count of detected price updates"
        INTEGER errors_count "Count of failed page/ad extractions"
    }

    PROPERTY {
        VARCHAR id_property PK "Unique ID from Otodom (e.g., ID64839)"
        VARCHAR name "Listing title"
        VARCHAR url "Full offer link"
        VARCHAR city "City"
        VARCHAR district "District"
        VARCHAR street "Street (if available)"
        INTEGER rooms "Number of rooms"
        REAL size "Area in sqm (REAL for SQLite)"
        INTEGER floor "Floor level (0 for parter)"
        VARCHAR market "primary / secondary"
        BOOLEAN is_active "1 if found in last scan, else 0"
        INTEGER first_scan_id FK "ID of the scan that first found it"
        INTEGER last_scan_id FK "ID of the most recent scan"
    }

    PRICE_HISTORY {
        INTEGER id PK "Auto-increment"
        VARCHAR id_property FK "Reference to PROPERTY"
        INTEGER id_scan FK "Which scan detected this price"
        TIMESTAMP timestamp "When the record was created"
        INTEGER price "Total price (INTEGER for PLN)"
        REAL price_per_m2 "Calculated price per sqm"
    }
