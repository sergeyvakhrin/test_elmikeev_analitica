# Generated by Django 5.1.3 on 2025-02-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testalmikeev", "0007_alter_googletab_total_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nm_id",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Продукт ID"
                    ),
                ),
                (
                    "report",
                    models.FloatField(blank=True, null=True, verbose_name="Сумма"),
                ),
            ],
            options={
                "verbose_name": "Отчет",
                "verbose_name_plural": "Отчеты",
            },
        ),
    ]
