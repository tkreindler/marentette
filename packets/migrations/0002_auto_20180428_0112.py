# Generated by Django 2.0.4 on 2018-04-28 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='chapterPacket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='packets.ChapterPacket'),
        ),
        migrations.AlterField(
            model_name='video',
            name='otherPacket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='packets.OtherPacket'),
        ),
    ]
