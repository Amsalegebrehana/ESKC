from asyncio import AbstractServer
from django.db import models

# Create your models here.
from django.db import models

class Admin(AbstractServer):
    username = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.username




class Applicant(models.Model):
    EDUCATION_LEVELS = (
        ('1', 'Beginner'),
        ('2', 'Beginner'),
        ('3', 'Beginner'),
        ('4','Beginner'),
        ('5', 'Beginner'),
        ('6', 'Beginner'),
        ('7', 'Beginner'),
        ('8', 'Beginner'),
        ('9', 'Intermediate'),
        ('10', 'Intermediate'),
        ('11', 'Advanced'),
        ('12', 'Advanced'),
    )

    firstName = models.CharField(max_length=255, blank=True)
    lastName = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=10, blank=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True)
    zone = models.CharField(max_length=255, blank=True)
    wereda = models.CharField(max_length=255, blank=True)
    parentFirstName = models.CharField(max_length=255, blank=True)
    parentLastName = models.CharField(max_length=255, blank=True)
    parentEmail = models.EmailField(blank=True)
    parentPhoneNumber = models.CharField(max_length=20, blank=True)
    schoolName = models.CharField(max_length=255, blank=True)
    schoolType = models.CharField(max_length=255, blank=True)
    schoolRegion = models.CharField(max_length=255, blank=True)
    schoolZone = models.CharField(max_length=255, blank=True)
    schoolWereda = models.CharField(max_length=255, blank=True)
    educationalLevel = models.CharField(max_length=255, blank=True, choices = EDUCATION_LEVELS, default='1')
    documentLink = models.URLField(blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    projectDetail = models.TextField(blank=True)
    selectedReadingRating = models.CharField(max_length=10, blank=True)
    languages = models.ManyToManyField('Language', related_name='applicants', blank=True)
    selectedWritingRating = models.CharField(max_length=10, blank=True)
    selectedListenRating = models.CharField(max_length=10, blank=True)
    selectedSpeakingRating = models.CharField(max_length=10, blank=True)
    selectedpLanguages = models.ManyToManyField('Language', blank=True)
    motivationDetail = models.TextField(blank=True)
    cvLink = models.URLField(blank=True)
    certificateLink = models.URLField(blank=True)
    recommendationLink = models.URLField(blank=True)
    orgs = models.ManyToManyField('Organization', blank=True)
    skillOption = models.CharField(max_length=255, blank=True)
    competition = models.CharField(max_length=255, blank=True)
    participation = models.CharField(max_length=255, blank=True)
    projectOption = models.CharField(max_length=255, blank=True)
    competitionOption = models.CharField(max_length=255, blank=True)
    selectedRating = models.CharField(max_length=10, blank=True)

    isAccepted = models.BooleanField(default=False)

    

    def __str__(self):
        return self.firstName + " " + self.lastName if self.lastName else self.firstName

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
