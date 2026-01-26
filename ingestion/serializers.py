from rest_framework import serializers
from customers.models import Customer

class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'customer_id',
            'first_name',
            'last_name',
            'age',
            'monthly_salary',
            'phone_number',
            'approved_limit'
        ]
        read_only_fields = ['customer_id', 'approved_limit']

    def create(self, validated_data):
        monthly_salary = validated_data.get('monthly_salary')
        approved_limit = round(monthly_salary * 36 / 100000) * 100000
        validated_data['approved_limit'] = approved_limit
        return super().create(validated_data)
