# Generated by Django 3.0.1 on 2020-02-17 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200216_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
    ]