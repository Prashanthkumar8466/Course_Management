# Generated by Django 3.2.25 on 2024-08-04 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_remove_enroll_details_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll_details',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
