import pandas as pd
from django.core.management.base import BaseCommand
from customers.models import Customer
from loans.models import Loan


class Command(BaseCommand):
    help = "Ingest customer and loan data from Excel files"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting data ingestion...")

        customer_df = pd.read_excel("customer_data.xlsx")

        for _, row in customer_df.iterrows():
            Customer.objects.update_or_create(
                customer_id=row["customer_id"],
                defaults={
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"],
                    "phone_number": row["phone_number"],
                    "monthly_salary": row["monthly_salary"],
                    "approved_limit": row["approved_limit"],
                },
            )

        self.stdout.write("Customers ingested successfully.")

        loan_df = pd.read_excel("loan_data.xlsx")

        for _, row in loan_df.iterrows():
            customer = Customer.objects.get(customer_id=row["customer_id"])

            Loan.objects.create(
                customer=customer,
                loan_amount=row["loan_amount"],
                interest_rate=row["interest_rate"],
                tenure=row["tenure"],
                emi=row["emi"],
                approved=row["approved"],
            )

        self.stdout.write(self.style.SUCCESS("Data ingestion completed."))
