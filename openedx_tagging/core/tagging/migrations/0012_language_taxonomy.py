# Generated by Django 3.2.19 on 2023-07-28 13:33

from django.core.management import call_command
from django.db import migrations
from django.db.models import Count


def create_language_taxonomy(apps, schema_editor):
    """
    Create language taxonomy
    """
    # Make sure the language taxonomy exists:
    Taxonomy = apps.get_model("oel_tagging", "Taxonomy")
    lang_taxonomy, _created = Taxonomy.objects.get_or_create(id=-1, defaults={
        "name": "Languages",
        "description": "Languages that are enabled on this system.",
        "enabled": True,
        "allow_multiple": False,
        "allow_free_text": False,
        "visible_to_authors": True,
        "_taxonomy_class": "openedx_tagging.core.tagging.models.system_defined.LanguageTaxonomy",
    })

    # But delete any unused tags created by the old fixture:
    lang_taxonomy.tag_set.annotate(usage_count=Count('objecttag')).filter(usage_count=0).delete()


def revert(apps, schema_editor):  # pragma: no cover
    """
    Deletes language taxonomy an tags
    """
    Taxonomy = apps.get_model("oel_tagging", "Taxonomy")
    Taxonomy.objects.filter(id=-1).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("oel_tagging", "0011_remove_required"),
    ]

    operations = [
        migrations.RunPython(create_language_taxonomy, revert),
    ]