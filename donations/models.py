import datetime
import django
from django.db import models

class Donation(models.Model):
    DONATION_OPTIONS = (
        ('cash', 'In Cash'),
        ('kind', 'In Kind'),
    )
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    donation_option = models.CharField(max_length=10, choices=DONATION_OPTIONS)
    created_date = models.DateField(auto_created=True,default=datetime.date.today)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
