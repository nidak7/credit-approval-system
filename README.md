# Credit Approval System – Backend Assignment

## Overview
This project is a **Credit Approval System backend** developed using **Django** and **Django Rest Framework**.  
It provides APIs to manage customers, evaluate loan eligibility, create loans, fetch loan details, and ingest bulk data from Excel files.

The entire application is **Dockerized**, making it easy to run without manual environment setup.

---

## Tech Stack
- Python 3.11
- Django
- Django Rest Framework
- SQLite
- Pandas, OpenPyXL
- Docker

---

## Project Structure
```
credit_approval_system/
│
├── customers/
│   ├── management/
│   │   └── commands/
│   │       └── ingest_data.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── loans/
│   ├── models.py
│   ├── serializers.py
│   ├── utils.py
│   ├── views.py
│   └── urls.py
│
├── credit_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── customer_data.xlsx
├── loan_data.xlsx
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── manage.py
└── README.md
```

---

## Features Implemented
- Customer registration with approved credit limit
- Loan eligibility check using credit score logic
- Loan creation with EMI calculation
- Fetch all loans of a customer
- Excel-based bulk data ingestion
- Fully Dockerized application

---

## API Endpoints

### Register Customer
```
POST /api/register/
```

### Check Loan Eligibility
```
POST /api/check-eligibility/
```

### Create Loan
```
POST /api/create-loan/
```

### Get Customer Loans
```
GET /api/customer-loans/<customer_id>/
```

---

## Sample Create Loan Request
```json
{
  "customer_id": 1,
  "loan_amount": 500000,
  "interest_rate": 10,
  "tenure": 24
}
```

---

## Excel Data Ingestion
The system supports bulk ingestion of customer and loan data from Excel files.

Files used:
- `customer_data.xlsx`
- `loan_data.xlsx`

Command used:
```bash
python manage.py ingest_data
```

---

## Running the Application with Docker

Build the Docker image:
```bash
docker build -t credit-approval-system .
```

Run the container:
```bash
docker run -p 8000:8000 credit-approval-system
```

Application runs at:
```
http://127.0.0.1:8000/
```

---

## Notes
- SQLite is used for simplicity
- Credit score and EMI calculations are handled in utility functions
- The system follows RESTful API design principles

---

## Author
**Nida Khan**
