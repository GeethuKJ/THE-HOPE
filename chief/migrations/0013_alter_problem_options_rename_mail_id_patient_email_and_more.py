# Generated by Django 5.0.3 on 2024-03-18 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0012_rename_case_patient_alter_patient_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ('title',), 'verbose_name': 'Problem', 'verbose_name_plural': 'Problems'},
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='mail_id',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='problem',
            old_name='question',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='posted_problems',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='total_problems_posted',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='case',
        ),
        migrations.AddField(
            model_name='problem',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problem', to='chief.patient'),
        ),
        migrations.AddField(
            model_name='problem',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='problem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='chief.patient'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='therapist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='chief.therapist'),
        ),
    ]
