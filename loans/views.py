from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from loans.serializers import LoanDetailSerializer
from customers.models import Customer
from loans.models import Loan
from loans.serializers import CheckEligibilitySerializer
from loans.serializers import CreateLoanSerializer
from loans.utils import calculate_credit_score, calculate_emi

class CheckEligibilityAPIView(APIView):

    def post(self, request):
        serializer = CheckEligibilitySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        customer_id = data["customer_id"]

        customer = Customer.objects.filter(customer_id=customer_id).first()
        if not customer:
            return Response(
                {"message": "Customer not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        credit_score = calculate_credit_score(customer)

        approval = False
        corrected_interest_rate = data["interest_rate"]

        if credit_score > 50:
            approval = True
        elif 30 < credit_score <= 50:
            approval = True
            corrected_interest_rate = max(corrected_interest_rate, 12)
        elif 10 < credit_score <= 30:
            approval = True
            corrected_interest_rate = max(corrected_interest_rate, 16)
        else:
            approval = False

        total_existing_emi = sum(
            loan.monthly_installment for loan in customer.loans.all()
        )

        if total_existing_emi > 0.5 * customer.monthly_salary:
            approval = False

        monthly_installment = calculate_emi(
            data["loan_amount"],
            corrected_interest_rate,
            data["tenure"]
        )

        return Response({
            "customer_id": customer.customer_id,
            "approval": approval,
            "interest_rate": data["interest_rate"],
            "corrected_interest_rate": corrected_interest_rate,
            "tenure": data["tenure"],
            "monthly_installment": monthly_installment
        })

class CreateLoanAPIView(APIView):
    

    def post(self, request):
        serializer = CreateLoanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        customer = Customer.objects.get(customer_id=data["customer_id"])

        credit_score = calculate_credit_score(customer)

        if credit_score < 600:
            return Response(
                {
                    "loan_approved": False,
                    "reason": "Credit score too low"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        emi = calculate_emi(
            data["loan_amount"],
            data["interest_rate"],
            data["tenure"]
        )

        loan = Loan.objects.create(
            customer=customer,
            loan_amount=data["loan_amount"],
            interest_rate=data["interest_rate"],
            tenure=data["tenure"],
            emi=emi,
            approved=True
        )

        return Response(
            {
                "loan_id": loan.loan_id,
                "customer_id": customer.customer_id,
                "loan_approved": True,
                "emi": emi
            },
            status=status.HTTP_201_CREATED
        )
        
class CustomerLoansAPIView(ListAPIView):
    serializer_class = LoanDetailSerializer

    def get_queryset(self):
        customer_id = self.kwargs["customer_id"]
        return Loan.objects.filter(customer__customer_id=customer_id)
    

    