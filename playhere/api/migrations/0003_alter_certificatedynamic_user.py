# Generated by Django 4.1 on 2023-04-27 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_certificatedynamic_output_certificate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatedynamic',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
