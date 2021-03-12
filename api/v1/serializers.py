from rest_framework import serializers

from insurance.models import Customer
from insurance.models import InsurancePolicy


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class InsurancePolicySerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(source='customer', queryset=Customer.objects.all())
    type = serializers.CharField(source='policy_type')

    class Meta:
        model = InsurancePolicy
        fields = ['customer_id', 'type', 'premium', 'cover']
