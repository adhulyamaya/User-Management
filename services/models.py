from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True, null=True) 
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.name
    
class Service(models.Model):

    SERVICE_TYPE_CHOICES = (
        ("customer", "Customer Service"),
        ("vendor", "Vendor Service"),
    )

    TAX_CHOICES = (
        ("GST_5", "5% GST"),
        ("GST_12", "12% GST"),
        ("GST_18", "18% GST"),
        ("GST_28", "28% GST"),
        ("none", "No Tax"),
    )

    hsn_code = models.CharField(max_length=10, blank=True, null=True)  # HSN/SAC Code
    quantity = models.PositiveIntegerField(default=1)   
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0) 
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)  
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="services")
    tax_rate = models.CharField(max_length=10, choices=TAX_CHOICES, default="none")  
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.name


