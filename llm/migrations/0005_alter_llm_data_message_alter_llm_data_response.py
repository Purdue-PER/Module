# Generated by Django 4.2 on 2023-10-16 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llm', '0004_alter_llm_data_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llm_data',
            name='message',
            field=models.CharField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='llm_data',
            name='response',
            field=models.CharField(max_length=50000),
        ),
    ]