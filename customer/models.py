from django.db import models
from main_admin.models import MainAdmin

class FinancialInfo(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)

    

class Customer(models.Model):
    company = models.ForeignKey(MainAdmin, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    purchase_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance_due = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False) 
    def __str__(self):
        return self.name

class Vendor(models.Model):
    company = models.ForeignKey(MainAdmin, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    is_deleted = models.BooleanField(default=False) 
    def __str__(self):
        return self.name
    


# When a staff enters sale/purchase details, the system will check if the customer/vendor already exists. 
# If not, it will create a new record for the customer/vendor and associate it with the sale/purchase



# from django.shortcuts import render, redirect
# from .models import Sale, Customer, Service
# from .forms import SaleForm

# def create_sale(request):
#     if request.method == "POST":
#         form = SaleForm(request.POST)
#         if form.is_valid():
#             # Get customer details from the form
#             customer_name = form.cleaned_data["customer_name"]
#             customer_email = form.cleaned_data["customer_email"]

#             # Check if customer exists, if not create a new one
#             customer, created = Customer.objects.get_or_create(
#                 email=customer_email,
#                 defaults={"name": customer_name}
#             )

#             # Create the sale record
#             service = form.cleaned_data["service"]
#             amount_paid = form.cleaned_data["amount_paid"]
#             payment_status = form.cleaned_data["payment_status"]

#             sale = Sale.objects.create(
#                 customer=customer,
#                 service=service,
#                 amount_paid=amount_paid,
#                 payment_status=payment_status,
#                 staff=request.user,  # Assuming staff is logged in and available
#             )
#             return redirect("sale_detail", pk=sale.pk)
#     else:
#         form = SaleForm()

#     return render(request, "sales/create_sale.html", {"form": form})
# def create_purchase(request):
#     if request.method == "POST":
#         form = PurchaseForm(request.POST)
#         if form.is_valid():
#             # Get vendor details from the form
#             vendor_name = form.cleaned_data["vendor_name"]
#             vendor_email = form.cleaned_data["vendor_email"]

#             # Check if vendor exists, if not create a new one
#             vendor, created = Vendor.objects.get_or_create(
#                 email=vendor_email,
#                 defaults={"name": vendor_name}
#             )

#             # Create the purchase record
#             service = form.cleaned_data["service"]
#             amount_paid = form.cleaned_data["amount_paid"]
#             payment_status = form.cleaned_data["payment_status"]

#             purchase = Purchase.objects.create(
#                 vendor=vendor,
#                 service=service,
#                 amount_paid=amount_paid,
#                 payment_status=payment_status,
#                 staff=request.user,  # Assuming staff is logged in and available
#             )
#             return redirect("purchase_detail", pk=purchase.pk)
#     else:
#         form = PurchaseForm()

#     return render(request, "purchases/create_purchase.html", {"form": form})
