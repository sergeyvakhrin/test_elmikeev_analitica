# Generated by Django 5.1.3 on 2025-02-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testalmikeev", "0005_alter_filecsv_options_alter_filecsv_file_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="googletab",
            name="total_price",
            field=models.IntegerField(blank=True, null=True, verbose_name="Сумма"),
        ),
    ]
