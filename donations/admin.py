from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'donation_option', 'created_date', 'contacted')
    list_filter = ('contacted','donation_option')
    search_fields = ('first_name','email',)

admin.site.register(Donation, DonationAdmin)
