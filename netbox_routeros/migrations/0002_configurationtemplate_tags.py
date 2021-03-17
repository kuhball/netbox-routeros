# Generated by Django 3.1.3 on 2021-03-07 11:23

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0053_rename_webhook_obj_type"),
        ("netbox_routeros", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="configurationtemplate",
            name="tags",
            field=taggit.managers.TaggableManager(
                through="extras.TaggedItem", to="extras.Tag"
            ),
        ),
    ]
