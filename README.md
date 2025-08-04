# 🕷️ UCLA Anderson Knapp Venture Competition Scraper

This project is a Scrapy-based Python crawler that extracts yearly winner details from the UCLA Anderson Knapp Venture Competition website. It parses business names and participant details for the top 3 winners each year (from 2020 back to 2014) and stores the data in Airtable.

---

## 🚀 Features

- Scrapes winner data (business + participants) from:
  - 2020 to 2014
- Extracts:
  - Year
  - Competition title
  - 1st, 2nd, and 3rd place business names
  - Participants' names
  - Last update timestamp
- Sends data directly to an Airtable table via the PyAirtable API.

---

## 🛠️ Requirements

- Python 3.7+
- Dependencies (install via `pip`):

```bash
pip install scrapy pyairtable
