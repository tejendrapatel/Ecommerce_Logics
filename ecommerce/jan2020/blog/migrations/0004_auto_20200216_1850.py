# Generated by Django 3.0.1 on 2020-02-17 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(max_length=300, null=True, upload_to=''),
        ),
    ]
