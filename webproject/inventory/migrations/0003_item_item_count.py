# Generated by Django 3.0.3 on 2020-05-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_itemmodel_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_count',
            field=models.IntegerField(default=0),
        ),
    ]
