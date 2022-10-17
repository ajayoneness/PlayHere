# Generated by Django 4.1 on 2022-10-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='category',
            field=models.TextField(default='coding', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='topic',
            field=models.TextField(default='python', max_length=250),
            preserve_default=False,
        ),
    ]
