# Generated by Django 2.1.7 on 2019-03-21 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20190321_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinaccount',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coin', to=settings.AUTH_USER_MODEL),
        ),
    ]
