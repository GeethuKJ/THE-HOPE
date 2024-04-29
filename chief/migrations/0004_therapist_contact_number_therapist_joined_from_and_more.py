# Generated by Django 5.0.3 on 2024-03-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0003_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapist',
            name='contact_number',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='therapist',
            name='joined_from',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='therapist',
            name='locatoin',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='therapist',
            name='mail_id',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='therapist',
            name='total_solutions_posted',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]