# Generated by Django 5.0.7 on 2024-10-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0002_remove_profile_phone_number_remove_profile_street_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile", old_name="phone", new_name="phone_number",
        ),
        migrations.AddField(
            model_name="profile",
            name="street",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]