# Generated by Django 3.0.3 on 2020-02-20 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200219_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='clg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.college'),
        ),
    ]
