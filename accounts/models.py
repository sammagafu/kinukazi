from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings
from django_resized import ResizedImageField


# Create your models here.
class Accounts(AbstractUser):
    TypeOfUser = [
        ('Normal Account','Normal Account'),
        ('Business Account','Business Account'),
    ]

    


    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    avatar = ResizedImageField(_("Avatar"),size=[300, 300], upload_to='user/avatars',crop=['middle', 'center'],quality=90)

class Business(models.Model):
    REGION = [
        ('Arusha', 'Arusha'),('Dar es Salaam', 'Dar es Salaam'),
        ('Dodoma', 'Dodoma'),('Geita', 'Geita'),
        ('Iringa', 'Iringa'),
        ('Kagera', 'Kagera'),
        ('Katavi', 'Katavi'),
        ('Kigoma', 'Kigoma'),
        ('Kilimanjaro', 'Kilimanjaro'),
        ('Lindi', 'Lindi'),
        ('Manyara', 'Manyara'),
        ('Mara', 'Mara'),
        ('Mbeya', 'Mbeya'),
        ('Mjini Magharibi', 'Mjini Magharibi'),
        ('Morogoro', 'Morogoro'),
        ('Mtwara', 'Mtwara'),
        ('Mwanza', 'Mwanza'),
        ('Njombe', 'Njombe'),
        ('Pemba North', 'Pemba North'),
        ('Pemba South', 'Pemba South'),
        ('Pwani', 'Pwani'),
        ('Rukwa', 'Rukwa'),
        ('Ruvuma', 'Ruvuma'),
        ('Shinyanga', 'Shinyanga'),
        ('Simiyu', 'Simiyu'),
        ('Singida', 'Singida'),
        ('Songwe', 'Songwe'),
        ('Tabora', 'Tabora'),
        ('Tanga', 'Tanga'),
        ('Unguja North', 'Unguja North'),
        ('Unguja South', 'Unguja South'),

    ]
    
    companyname = models.CharField(_("Business Name"), max_length=180)
    region = models.CharField(_("Business Location"), max_length=50,choices=REGION)
    address = models.TextField(_("Business Address"))
    contactperson = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    companywebsite = models.URLField(_("Company Website"),null=True,blank=True)
    companyemail = models.EmailField(_("Company Email Address"))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    logo = ResizedImageField(_("Company Logo"),size=[300, 300], upload_to='user/avatars',crop=['middle', 'center'],quality=90)

