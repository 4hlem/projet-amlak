# Generated by Django 5.0 on 2023-12-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_companyprofile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='individualprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
