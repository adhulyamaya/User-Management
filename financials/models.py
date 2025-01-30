from django.db import models
from services.models import Service
from customer.models import Customer,Vendor


# (sales and purchases tracking)
# class ServiceTransaction(models.Model):
#     CUSTOMER = "customer"
#     VENDOR = "vendor"

#     TRANSACTION_TYPE_CHOICES = (
#         (CUSTOMER, "Customer"),
#         (VENDOR, "Vendor"),
#     )

#     PAYMENT_STATUS_CHOICES = (
#     ("paid", "Paid"),
#     ("unpaid", "Unpaid"),
#     ("completely_paid", "Completely Paid"),
#     ("pending", "Pending"),
#     )

#     PAYMENT_MODE_CHOICES = (
#     ("cash", "Cash"),
#     ("cheque", "Cheque"),
#     ("upi", "UPI"),
#     ("other", "Other"),
#     )

#     transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
#     customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, related_name="transactions")
#     vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, null=True, blank=True, related_name="transactions")
#     service = models.ForeignKey('Service', on_delete=models.CASCADE)
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES)
    # payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES, blank=True, null=True)
    # tax_rate = models.CharField(max_length=10, choices=Service.TAX_CHOICES, default="none")

#     def __str__(self):
#         if self.transaction_type == "customer" and self.customer:
#             return f"{self.customer.name} - {self.service.name}"
#         elif self.transaction_type == "vendor" and self.vendor:
#             return f"{self.vendor.name} - {self.service.name}"
#         return f"Transaction for {self.service.name}"



PAYMENT_STATUS_CHOICES = (
    ("paid", "Paid"),
    ("unpaid", "Unpaid"),
    ("completely_paid", "Completely Paid"),
    ("pending", "Pending"),
)

PAYMENT_MODE_CHOICES = (
    ("cash", "Cash"),
    ("cheque", "Cheque"),
    ("upi", "UPI"),
    ("other", "Other"),
)

# Sales Model
class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES)
    sale_date = models.DateField(auto_now_add=True)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES, blank=True, null=True)
    tax_rate = models.CharField(max_length=10, choices=Service.TAX_CHOICES, default="none")

    def __str__(self):
        return f"Sale of {self.service.name} to {self.customer.name}"

# Purchases Model
class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES)
    purchase_date = models.DateField(auto_now_add=True)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES, blank=True, null=True)
    tax_rate = models.CharField(max_length=10, choices=Service.TAX_CHOICES, default="none")

    def __str__(self):
        return f"Purchase of {self.service.name} from {self.vendor.name}"



# from django.db import models
# from services.models import Service
# from customer.models import Customer, Vendor

# class Sale(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Added
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#     balance_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Added
#     payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES)
#     sale_date = models.DateField(auto_now_add=True)
#     payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES, blank=True, null=True)
#     tax_rate = models.CharField(max_length=10, choices=Service.TAX_CHOICES, default="none")
#     remarks = models.TextField(blank=True, null=True)  # Added for any additional notes

#     def save(self, *args, **kwargs):
#         if not self.balance_amount:
#             self.balance_amount = self.total_amount - self.amount_paid
#         super().save(*args, **kwargs)

# class Purchase(models.Model):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Added
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#     balance_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Added
#     payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES)
#     purchase_date = models.DateField(auto_now_add=True)
#     payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES, blank=True, null=True)
#     tax_rate = models.CharField(max_length=10, choices=Service.TAX_CHOICES, default="none")
#     remarks = models.TextField(blank=True, null=True)  # Added for any additional notes

#     def save(self, *args, **kwargs):
#         if not self.balance_amount:
#             self.balance_amount = self.total_amount - self.amount_paid
#         super().save(*args, **kwargs)