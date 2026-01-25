from datetime import date
from math import pow
from loans.models import Loan


def calculate_credit_score(customer):
    score = 600  # base score for registered customer

    # Income-based scoring (USE monthly_salary)
    if customer.monthly_salary >= 50000:
        score += 150
    elif customer.monthly_salary >= 30000:
        score += 100
    else:
        score += 50

    # Age-based stability
    if customer.age >= 25:
        score += 50

    return min(score, 900)


def calculate_emi(principal, annual_rate, tenure):
    monthly_rate = annual_rate / (12 * 100)
    emi = principal * monthly_rate * pow(1 + monthly_rate, tenure) / (pow(1 + monthly_rate, tenure) - 1)
    return round(emi, 2)
