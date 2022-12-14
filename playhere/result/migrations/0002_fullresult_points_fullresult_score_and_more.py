# Generated by Django 4.1 on 2022-12-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullresult',
            name='points',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fullresult',
            name='score',
            field=models.IntegerField(default=0.1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fullresult',
            name='time_taken',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
