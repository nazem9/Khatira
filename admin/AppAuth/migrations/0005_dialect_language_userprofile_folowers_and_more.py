# Generated by Django 5.0.1 on 2024-02-07 13:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAuth', '0004_alter_userprofile_accessibilty_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialect', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='folowers',
            field=models.ManyToManyField(blank=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dialect',
            field=models.ManyToManyField(null=True, to='AppAuth.dialect'),
        ),
        migrations.AddField(
            model_name='dialect',
            name='language',
            field=models.ManyToManyField(null=True, related_name='dialect_language', to='AppAuth.language'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='languages',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppAuth.language'),
        ),
    ]
