from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

class Client(models.Model):
    nom = models.CharField(max_length=100, blank=False, null=False)
    prenom = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone = PhoneNumberField(blank=False, null=False)
    country = CountryField(blank=False, null=False)
    city = models.CharField(max_length=200, blank=False, null=False)
    neighboarhood = models.CharField(max_length=200, blank=False, null=False)
    address_description = models.TextField(max_length= 250, blank=True, null=True)


class Business(models.Model):
    business_name = models.CharField(max_length=100, blank=False, null=False)
    business_country = CountryField(blank=False, null=False)
    business_city = models.CharField(max_length=200, blank=False, null=False)
    business_neighboarhood = models.CharField(max_length=200, blank=False, null=False)
    business_address_description = models.TextField(max_length= 250, blank=True, null=True)
    creation_year = models.IntegerField(max_length=6, blank=False, null=False)
    is_certified  = models.BooleanField(null= False, blank=True)

    # Manager fields
    manager_nom = models.CharField(max_length=150, blank=False, null=False)
    manager_prenom = models.CharField(max_length=150, blank=False, null=False)
    manager_email = models.EmailField(max_length=100, blank=False, null=False)
    manager_phone = PhoneNumberField(blank=False, null=False)
    manager_title = models.CharField(max_length=200, blank=False, null=False)
   
    # Subscription 
    class SUBSCRIPTION(models.TextChoices):
        BASIC = 'Basique',
        PRO = 'Professionnel',
        ENTREPRISE = 'Entreprise',
    subscription_plan = models.CharField(choices=SUBSCRIPTION.choices, blank=False, null=False)

    #Payment
    class PAYMENT(models.TextChoices):
        OM = 'Orange Money',
        MOMO ='MTN Mobile Money',
    payment_details = models.CharField(choices=PAYMENT.choices, blank=False, null=False)

class CabinetDArchitechture(Business):
    cabinet_email = models.EmailField(max_length=100, blank=False, null=False)
    cabinet_phone = PhoneNumberField(blank=False, null=False)
    cabinet_description = models.TextField(max_length= 500, blank=True, null=True)
    manager_professional_qualifications = models.TextField(blank=True, null=True)

    # Activities 
    activities = models.JSONField(default=list, blank=False, null=False)  # List of selected activities


class SocieteImmobiliere(Business):
    licence_number = models.CharField(max_length=200, blank=False, null=False)
    # Properties
    properties_type = models.JSONField(default=list, blank=False, null=False)  # List of selected activities