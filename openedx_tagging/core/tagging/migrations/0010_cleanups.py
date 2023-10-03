# Generated by Django 3.2.19 on 2023-09-29 16:59

import django.db.models.expressions
from django.db import migrations, models

import openedx_learning.lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oel_tagging', '0009_alter_objecttag_object_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ModelObjectTag',
        ),
        migrations.DeleteModel(
            name='UserModelObjectTag',
        ),
        migrations.AlterUniqueTogether(
            name='objecttag',
            unique_together={('object_id', 'taxonomy', 'tag_id'), ('object_id', 'taxonomy', '_value')},
        ),
        # ObjectTag.Tag can be blank
        migrations.AlterField(
            model_name='objecttag',
            name='tag',
            field=models.ForeignKey(blank=True, default=None, help_text="Tag associated with this object tag. Provides the tag's 'value' if set.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='oel_tagging.tag'),
        ),
    ]
