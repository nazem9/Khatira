# Generated by Django 5.0.1 on 2024-02-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAuth', '0003_alter_userprofile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='accessibilty',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='languages',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(max_length=50, null=True),
        ),
    ]