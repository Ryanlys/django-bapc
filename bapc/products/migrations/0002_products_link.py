# Generated by Django 3.1.7 on 2021-02-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='link',
            field=models.TextField(default=''),
        ),
    ]