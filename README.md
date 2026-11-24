# Credit Approval System

This is a Django REST backend for a loan assignment. A customer can be registered and checked for loan eligibility, a loan can be created with a monthly installment (EMI), and a customer's loans can be listed.

## What it does

- `POST /api/register/` creates a customer with an approved credit limit
- `POST /api/check-eligibility/` returns an approval decision and a corrected interest rate based on a credit score
- `POST /api/create-loan/` creates a loan and calculates the EMI
- `GET /api/customer-loans/<customer_id>/` lists a customer's loans
- A management command loads customer and loan data from the two Excel files in the repo

## Tech used

Python 3.11, Django, Django REST Framework, SQLite, Pandas, OpenPyXL, Docker

## How to run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py ingest_data
python manage.py runserver
```

With Docker:

```bash
docker build -t credit-approval-system .
docker run -p 8000:8000 credit-approval-system
```

The Dockerfile only starts the server, so `migrate` and `ingest_data` have to be run inside the container as well.

Settings read `DJANGO_SECRET_KEY` and `DJANGO_DEBUG` from the environment. If they are not set, a local dev key is used and `DEBUG` is on, which is fine for running it locally only.

## What I would improve

- The credit score is a simple rule on salary and age, not a real scoring model
- The ingest command exists in two places (`ingestion` and `customers`), I would keep one
- The test files are empty
