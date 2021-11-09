# Generated by Django 3.2.9 on 2021-11-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]