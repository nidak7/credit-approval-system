from django.db import models
from customers.models import Customer

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    tenure = models.IntegerField()
    emi = models.FloatField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Loan {self.loan_id} - {self.customer}"
