from django.contrib import admin
from .models import Applicant, Skill, Language, Organization


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1


class OrganizationInline(admin.TabularInline):
    model = Organization
    extra = 1


class ApplicantAdmin(admin.ModelAdmin):
    # inlines = [SkillInline, LanguageInline, OrganizationInline]
    list_display = ['firstName', 'lastName', 'email', 'phoneNumber', 'dateOfBirth']
    list_filter = ['region', 'zone', 'wereda']
    search_fields = ['firstName', 'lastName', 'email', 'phoneNumber', 'region', 'zone', 'wereda']


admin.site.register(Applicant, ApplicantAdmin)
