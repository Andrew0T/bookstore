# Generated by Django 4.2.2 on 2023-07-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_sale_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date_create',
            field=models.DateField(auto_now_add=True),
        ),
    ]
