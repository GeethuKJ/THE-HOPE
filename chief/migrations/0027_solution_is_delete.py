# Generated by Django 5.0.3 on 2024-05-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0026_patient_profile_image_therapist_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
