# Generated by Django 5.0.3 on 2024-03-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0015_remove_patient_profile_patient_user_therapist_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ('patient_id',), 'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='case_id',
            new_name='patient_id',
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='therapist',
            name='password',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='joined_from',
            field=models.DateTimeField(max_length=100),
        ),
    ]