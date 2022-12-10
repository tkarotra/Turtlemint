from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50, default="")

class Model(models.Model):
    make = models.ForeignKey(Company, on_delete=models.SET_DEFAULT, default="1")
    model = models.CharField(max_length=50, default="")
    year = models.IntegerField(default="")
    engine_fuel_type = models.CharField(max_length=100, default="")
    engine_hp = models.IntegerField(default="")
    engine_cylinders = models.IntegerField(default="")
    transmission_type = models.CharField(max_length=30, default="")
    driven_wheels = models.CharField(max_length=30, default="")
    no_of_doors = models.IntegerField(default="")
    market_category = models.CharField(max_length=100, default="")
    vehicle_size = models.CharField(max_length=20, default="")
    vehicle_style = models.CharField(max_length=30, default="")
    highway_mpg = models.IntegerField(default="")
    city_mpg = models.IntegerField(default="")
    msrp = models.IntegerField(default="")

class Policy(models.Model):
    display_name = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=300, default="")
    parent_plan = models.CharField(max_length=100, default="")
    net_premium = models.CharField(max_length=100, default="")
    gross_premium = models.CharField(max_length=100, default="")
    cgst = models.CharField(max_length=50, default="")
    sgst = models.CharField(max_length=50, default="")
    gst = models.CharField(max_length=50, default="")
    net_strike_through_premium = models.CharField(max_length=50, default="")
    covered_display_name = models.CharField(max_length=100, default="")
    not_covered_display_name = models.CharField(max_length=100, default="")
    covered_description = models.CharField(max_length=100, default="")
    not_covered_description = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=10, default="")