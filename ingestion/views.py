# ingestion/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerRegisterSerializer  # your serializer
from customers.models import Customer


class RegisterCustomer(APIView):

    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()  # Saves and returns the model instance
            return Response(
                {
                    "customer_id": customer.customer_id,  # Correct PK
                    "name": f"{customer.first_name} {customer.last_name}",
                    "age": customer.age,
                    "monthly_income": customer.monthly_salary,  # matches model
                    "approved_limit": customer.approved_limit,
                    "phone_number": customer.phone_number,
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
