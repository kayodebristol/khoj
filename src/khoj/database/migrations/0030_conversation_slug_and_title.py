# Generated by Django 4.2.7 on 2024-02-05 04:39

from django.db import migrations, models


def set_default_slug(apps, schema_editor):
    Conversation = apps.get_model("database", "Conversation")
    for conversation in Conversation.objects.all():
        formatted_date = conversation.created_at.strftime("%Y-%m-%d")
        conversation.slug = f"Conversation from {formatted_date}"
        conversation.save()


def reverse_set_default_slug(apps, schema_editor):
    Conversation = apps.get_model("database", "Conversation")
    for conversation in Conversation.objects.all():
        conversation.slug = None
        conversation.save()


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0029_userrequests"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversation",
            name="slug",
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="conversation",
            name="title",
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.RunPython(set_default_slug, reverse_code=reverse_set_default_slug),
    ]