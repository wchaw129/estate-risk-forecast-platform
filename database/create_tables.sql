CREATE TABLE SCAN_LOGS(  
    id_scan SERIAL PRIMARY KEY,
    start_time timestamp NOT NULL,
    end_time timestamp,
    offers_found INTEGER DEFAULT 0,
    new_offers INTEGER DEFAULT 0,
    price_changes INTEGER DEFAULT 0,
    errors_count INTEGER DEFAULT 0
);

CREATE TABLE PROPERTY (
    id_property SERIAL PRIMARY KEY,
    ad_id VARCHAR(20) UNIQUE,
    ad_name VARCHAR(255),
    ad_url VARCHAR(255),
    place VARCHAR(255),
    rooms INTEGER,
    property_size NUMERIC(10, 2),
    floor INTEGER,
    market VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    first_scan_id INTEGER DEFAULT NULL REFERENCES SCAN_LOGS(id_scan),
    last_scan_id INTEGER DEFAULT NULL REFERENCES SCAN_LOGS(id_scan)
);

CREATE TABLE PRICE_HISTORY(
    id_price SERIAL PRIMARY KEY,
    ad_id VARCHAR(20) NOT NULL REFERENCES PROPERTY(ad_id),
    id_scan INTEGER DEFAULT NULL REFERENCES SCAN_LOGS(id_scan),
    cur_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    price INTEGER,
    currency VARCHAR(10) DEFAULT 'PLN'
);

