from django.core.management.base import BaseCommand
import pandas as pd

from customers.models import Customer
from loans.models import Loan


class Command(BaseCommand):
    help = "Ingest customer and loan data from Excel files"

    def handle(self, *args, **options):
        self.stdout.write("Starting customer data ingestion...")
        self.ingest_customers()
        self.stdout.write(self.style.SUCCESS("Customer ingestion completed successfully."))

        self.stdout.write("Starting loan data ingestion...")
        self.ingest_loans()
        self.stdout.write(self.style.SUCCESS("Loan ingestion completed successfully."))

    def ingest_customers(self):
        df = pd.read_excel("customer_data.xlsx")

        for _, row in df.iterrows():
            Customer.objects.create(
                first_name=row["First Name"],
                last_name=row["Last Name"],
                age=row["Age"],
                phone_number=str(row["Phone Number"]),
                monthly_salary=row["Monthly Salary"],
                approved_limit=row["Approved Limit"],
            )

    def ingest_loans(self):
        df = pd.read_excel("loan_data.xlsx")

        for _, row in df.iterrows():
            customer = Customer.objects.get(customer_id=row["Customer ID"])

            Loan.objects.create(
                customer=customer,
                loan_amount=row["Loan Amount"],
                interest_rate=row["Interest Rate"],
                tenure=row["Tenure"],
                emi=row["Monthly payment"],
                approved=True
            )
