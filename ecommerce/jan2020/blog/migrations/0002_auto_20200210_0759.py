# Generated by Django 3.0.3 on 2020-02-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='college',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
