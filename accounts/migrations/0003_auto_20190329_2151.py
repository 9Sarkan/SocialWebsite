# Generated by Django 2.1.7 on 2019-03-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190327_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='nuser',
            name='facebook',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nuser',
            name='instagram',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nuser',
            name='twitter',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nuser',
            name='youtube',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]