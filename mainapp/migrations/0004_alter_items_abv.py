# Generated by Django 5.0.7 on 2024-08-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_rename_beer_items_rename_beer_cartitem_items_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="abv",
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]