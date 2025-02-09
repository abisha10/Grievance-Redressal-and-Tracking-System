# Generated by Django 5.1.5 on 2025-01-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_complaint_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
