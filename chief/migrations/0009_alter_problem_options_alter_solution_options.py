# Generated by Django 5.0.3 on 2024-03-18 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0008_problem_solution'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ('case',), 'verbose_name': 'Problem', 'verbose_name_plural': 'Problems'},
        ),
        migrations.AlterModelOptions(
            name='solution',
            options={'ordering': ('therapist',), 'verbose_name': 'Solution', 'verbose_name_plural': 'Solutions'},
        ),
    ]