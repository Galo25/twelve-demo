# Generated by Django 3.0.7 on 2022-04-02 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0029_auto_20210220_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 10, 43, 46, 51210)),
        ),
    ]