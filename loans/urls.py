from django.urls import path
from .views import CheckEligibilityAPIView, CreateLoanAPIView, CustomerLoansAPIView

urlpatterns = [
    path("check-eligibility/", CheckEligibilityAPIView.as_view()),
    path("create-loan/", CreateLoanAPIView.as_view()),
    path("customer-loans/<int:customer_id>/", CustomerLoansAPIView.as_view()),
]
