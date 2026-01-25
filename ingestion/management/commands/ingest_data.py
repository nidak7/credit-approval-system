from django.core.management.base import BaseCommand
from ingestion.tasks import ingest_customer_data, ingest_loan_data

class Command(BaseCommand):
    help = "Ingest customer and loan data from Excel files"

    def handle(self, *args, **kwargs):
        ingest_customer_data()
        ingest_loan_data()
        self.stdout.write(
            self.style.SUCCESS("Excel data ingested successfully")
        )