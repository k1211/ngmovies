# Generated by Django 2.1 on 2018-08-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20180807_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]