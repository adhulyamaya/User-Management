# Generated by Django 5.1.5 on 2025-01-29 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid'), ('completely_paid', 'Completely Paid'), ('pending', 'Pending')], max_length=50)),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('payment_mode', models.CharField(blank=True, choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI'), ('other', 'Other')], max_length=20, null=True)),
                ('tax_rate', models.CharField(choices=[('GST_5', '5% GST'), ('GST_12', '12% GST'), ('GST_18', '18% GST'), ('GST_28', '28% GST'), ('none', 'No Tax')], default='none', max_length=10)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid'), ('completely_paid', 'Completely Paid'), ('pending', 'Pending')], max_length=50)),
                ('sale_date', models.DateField(auto_now_add=True)),
                ('payment_mode', models.CharField(blank=True, choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI'), ('other', 'Other')], max_length=20, null=True)),
                ('tax_rate', models.CharField(choices=[('GST_5', '5% GST'), ('GST_12', '12% GST'), ('GST_18', '18% GST'), ('GST_28', '28% GST'), ('none', 'No Tax')], default='none', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
        ),
    ]
