# Generated by Django 3.0.1 on 2020-02-17 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200210_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
    ]