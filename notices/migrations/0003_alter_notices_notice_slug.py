# Generated by Django 4.2.4 on 2023-09-02 18:42

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_notices_notice_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='notice_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='notice_title', unique=True),
        ),
    ]
