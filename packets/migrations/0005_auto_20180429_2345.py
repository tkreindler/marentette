# Generated by Django 2.0.4 on 2018-04-29 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packets', '0004_auto_20180429_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterpacket',
            name='number',
            field=models.IntegerField(),
        ),
    ]
