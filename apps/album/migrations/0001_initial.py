# Generated by Django 2.1 on 2019-12-26 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        editable=False,
                        help_text="主キー",
                        primary_key=True,
                        serialize=False,
                        verbose_name="主キー",
                    ),
                ),
                ("image", models.ImageField(upload_to="")),
                ("memo", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
