# Generated by Django 4.1 on 2023-02-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_remove_addmore_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.TextField()),
                ('subcat_name', models.TextField()),
            ],
        ),
    ]