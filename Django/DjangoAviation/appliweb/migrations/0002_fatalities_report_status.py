# Generated by Django 2.2.5 on 2020-04-14 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatalities_report',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
