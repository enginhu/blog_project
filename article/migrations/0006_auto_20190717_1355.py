# Generated by Django 2.2.3 on 2019-07-17 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20190717_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
    ]
