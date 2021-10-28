# Generated by Django 3.2.8 on 2021-10-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name="Product's Name")),
                ('brand', models.CharField(max_length=40, verbose_name="Product's Brand")),
                ('price', models.FloatField(verbose_name="Product's Price")),
                ('qty', models.IntegerField(default=1, verbose_name='Quantity')),
                ('warranty', models.IntegerField(default=1, verbose_name='Warranty in months')),
            ],
        ),
    ]
