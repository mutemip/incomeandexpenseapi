# Generated by Django 3.2.7 on 2021-09-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20210910_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('OTHERS', 'OTHERS'), ('FOOD', 'FOOD'), ('TRAVEL', 'TRAVEL'), ('RENT', 'RENT'), ('ONLINE_SERVICES', 'ONLINE_SERVICES')], max_length=255),
        ),
    ]
