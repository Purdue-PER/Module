# Generated by Django 3.2.8 on 2021-12-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Force_HLG', '0018_auto_20211217_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='vectorslog',
            name='videoNumber',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]