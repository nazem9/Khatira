# Generated by Django 5.0.1 on 2024-02-07 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAuth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
