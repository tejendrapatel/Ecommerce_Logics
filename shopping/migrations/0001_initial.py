# Generated by Django 3.0.3 on 2020-03-06 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subname', models.CharField(max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(max_length=200)),
                ('proprice', models.FloatField()),
                ('prodescription', models.TextField()),
                ('prodiscount', models.CharField(max_length=20)),
                ('prospecification', models.TextField()),
                ('proimage', models.FileField(null=True, upload_to='')),
                ('proimage2', models.FileField(null=True, upload_to='')),
                ('proimage3', models.FileField(null=True, upload_to='')),
                ('proimage4', models.FileField(null=True, upload_to='')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.Subcategory')),
            ],
        ),
    ]
