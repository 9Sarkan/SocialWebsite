# Generated by Django 2.1.7 on 2019-03-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190329_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(help_text='Please select or just created tags related to this post.', to='posts.Tag'),
        ),
    ]
