# Generated by Django 4.1.3 on 2023-09-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0010_rename_name_python_joiners_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='python_joiners',
            name='email_id',
            field=models.EmailField(max_length=30),
        ),
    ]