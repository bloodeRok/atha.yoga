# Generated by Django 4.1.5 on 2023-01-15 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0004_alter_article_seo_description_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="category",
            unique_together={("parent", "slug")},
        ),
    ]