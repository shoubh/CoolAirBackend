# Generated by Django 2.1.7 on 2019-03-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20190326_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='url',
            field=models.URLField(default='http://localhost:8000/airports/', max_length=250),
            preserve_default=False,
        ),
    ]
