# Generated by Django 2.0.9 on 2018-12-06 02:25

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='missionstatement',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='origin_statement',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]