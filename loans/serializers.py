from rest_framework import serializers
from loans.models import Loan

class CheckEligibilitySerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    loan_amount = serializers.FloatField()
    interest_rate = serializers.FloatField()
    tenure = serializers.IntegerField()

class CreateLoanSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    loan_amount = serializers.FloatField()
    interest_rate = serializers.FloatField()
    tenure = serializers.IntegerField()
    
class LoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "loan_id",
            "loan_amount",
            "interest_rate",
            "tenure",
            "emi",
            "approved"
        ]