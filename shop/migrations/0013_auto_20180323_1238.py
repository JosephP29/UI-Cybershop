# Generated by Django 2.0.2 on 2018-03-23 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_merge_20180323_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyreceipt',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
