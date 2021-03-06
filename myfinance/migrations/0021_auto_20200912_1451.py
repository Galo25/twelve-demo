# Generated by Django 3.0.7 on 2020-09-12 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myfinance', '0020_auto_20200829_1718'),
    ]

    operations = [
        migrations.RenameModel('PlaidUser', 'PlaidItem'),
        migrations.AddField(
            model_name='plaiditem',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myfinance.Account'),
        ),
        migrations.AlterField(
            model_name='plaiditem',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
