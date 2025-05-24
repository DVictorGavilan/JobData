# 📊 JobData

## 🚀 Project Overview

This project is a **Python-based web scraper and ETL pipeline** designed to collect job offer data from **multiple job portals**. It is built with scalability in mind to support scraping from various employment websites. 

Currently, the implementation supports:
- **[Tecnoempleo](https://www.tecnoempleo.com)** (a leading Spanish tech job board).

It covers the full data pipeline:

- Web scraping of job listings
- ETL process (Extract → Transform → Load)
- Data quality validation using custom-defined rules
- Automated unit tests to ensure reliability and maintainability

The final dataset is stored in **CSV format**, ready for data analysis or integration into business intelligence systems.

For any bugs or questions, please contact [Dani Gavilán](mailto:danigavipedro96@gmail.com).

---

## 🛠️ Technologies Used

- **Python 3**
- **BeautifulSoup4** – HTML parsing
- **Requests** – HTTP requests
- **Pandas** – Data transformation and CSV export
- **Pytest** – Unit testing framework
- **DataQualityKit** – To ensure data quality

---

## 🧠 Features

- Handles pagination to scrape multiple job listing pages
- Extracts structured fields:
  - Job URL
  - Job Title
  - Job Company
  - Technologies/Skills
  - Required Experience
  - Posting Date
  - Location
  - Workplace Location
  - Salary Lower Bound
  - Salary Upper Bound
- Applies **data quality checks**:
  - No empty mandatory fields
  - Format validation
- Exports cleaned data to a `.csv` file
- Includes a **test suite** to validate scraper and ETL logic

---

## ⚙️ How to Run

1. Clone the repository:

```bash
  git clone https://github.com/your-username/tecnoempleo-job-scraper.git
  cd tecnoempleo-job-scraper
```

2. Create a virtual environment (optional but recommended):

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
  pip install -r requirements.txt
```

4. Run the scraper and ETL process:
```bash
  python main.py
```

5. Run tests to verify functionality:

```bash
  pytest tests/
```

---

## 📁 Sample Output

```csv
job_url,job_name,job_company,job_technologies_stack,job_description,publication_date,city,workplace_location,has_been_updated,salary_lower_bound,salary_upper_bound,cutoff_date
https://www.tecnoempleo.com/job-name/net/rf-5fc1,Job Name ,Job Company,"['React', 'TypeScript', 'GraphQL']",Job description ...,2025-05-23,Málaga,Híbrido,False,30000.0,33000.0,2025-05-24
...
```
---


## 📂 Project Structure

```bash
  JobData/
  ├── data/
  │   ├── master/            # Output CSV file with clean job data
  │   └── raw/               # Output CSV file with clean raw data
  ├── job_data/
  │   ├── scraper.py         # Main script for scraping
  │   ├── processing.py      # Main script for processing
  │   ├── quality.py         # Main script for data quality validations
  │   └── pipeline.py        # Main script for pipeline
  ├── tests/
  │   ├── test_scraper.py    # Unit tests for scraping logic
  │   ├── test_processing.py # Unit tests for processing logic
  │   ├── test_quality.py    # Unit tests for data quality validations logic
  │   └── test_pipeline.py   # Unit tests for pipeline logic
  ├── main.py                # Main script
  ├── requirements.txt       # Python dependencies
  ├── CHANGELOG.md           # Project documentation
  └── README.md              # Project documentation
```

---