# Generated by Django 4.1.3 on 2023-08-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
