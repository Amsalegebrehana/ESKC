# Generated by Django 4.2.3 on 2023-07-12 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='certificateLink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='competition',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='competitionOption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='cvLink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='documentLink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='educationalLevel',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='firstName',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='applicants', to='user.language'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='lastName',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='motivationDetail',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='orgs',
            field=models.ManyToManyField(blank=True, to='user.organization'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='parentEmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='parentFirstName',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='parentLastName',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='parentPhoneNumber',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='participation',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='projectDetail',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='projectOption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='recommendationLink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='region',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='schoolName',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='schoolRegion',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='schoolType',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='schoolWereda',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='schoolZone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='selectedListenRating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='selectedRating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='selectedReadingRating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='selectedSpeakingRating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='selectedWritingRating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='selectedpLanguages',
            field=models.ManyToManyField(blank=True, to='user.language'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='sex',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='skillOption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='skills',
            field=models.ManyToManyField(blank=True, to='user.skill'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='wereda',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='zone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
