# Generated by Django 3.1.4 on 2021-02-20 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0028_auto_20210220_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 20, 8, 33, 30, 456190)),
        ),
    ]