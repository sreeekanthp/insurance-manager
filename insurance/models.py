from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class InsurancePolicy(models.Model):
    POLICY_TYPES = (("personal-accident", "Personal Accident"),)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=100, choices=POLICY_TYPES)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.customer} - {self.get_policy_type_display()}"
