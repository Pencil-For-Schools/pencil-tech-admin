# Generated by Django 4.2.3 on 2024-09-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='sales_force_id',
        ),
        migrations.AddField(
            model_name='school',
            name='sales_force_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
