# Generated by Django 5.0.3 on 2024-05-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0025_patient_age_patient_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AddField(
            model_name='therapist',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
