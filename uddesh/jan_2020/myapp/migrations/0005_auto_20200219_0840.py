# Generated by Django 3.0.2 on 2020-02-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_students_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
