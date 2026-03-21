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
    PROPERTY ||--o{ PRICE_HISTORY : "has"
    PROPERTY {
        VARCHAR id_property PK "Unique ID from listing URL"
        VARCHAR name "Listing title"
        VARCHAR url "Full offer link"
        VARCHAR province "Voivodeship"
        VARCHAR city "City"
        VARCHAR district "District"
        VARCHAR street "Street (optional)"
        INTEGER rooms "Number of rooms"
        FLOAT size "Area in sqm"
        VARCHAR market "Market type (primary/secondary)"
        BOOLEAN is_active "Activity status"
        TIMESTAMP last_seen "Last scrape timestamp"
    }
    PRICE_HISTORY {
        INTEGER id PK "Auto-increment"
        VARCHAR id_property FK "Reference to PROPERTY"
        TIMESTAMP date "Price record timestamp"
        DECIMAL price "Total price"
        DECIMAL price_per_m2 "Price per square meter"
    }
    LOGS {
        INTEGER id_scan PK "Auto-increment"
        TIMESTAMP start_time "Process start"
        TIMESTAMP end_time "Process end"
        INTEGER offers_found "Count of organic listings"
        INTEGER errors_count "Count of failed extractions"
    }
