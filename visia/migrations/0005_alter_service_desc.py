# Generated by Django 4.1.3 on 2023-02-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visia', '0004_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='desc',
            field=models.TextField(max_length=250),
        ),
    ]