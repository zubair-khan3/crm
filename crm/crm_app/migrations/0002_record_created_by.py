# Generated by Django 4.2.5 on 2023-10-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='created_by',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
