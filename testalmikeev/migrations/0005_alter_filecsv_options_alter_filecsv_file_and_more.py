# Generated by Django 5.1.3 on 2025-02-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testalmikeev", "0004_filecsv"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="filecsv",
            options={"verbose_name": "Файл", "verbose_name_plural": "Файлы"},
        ),
        migrations.AlterField(
            model_name="filecsv",
            name="file",
            field=models.FileField(
                blank=True,
                default=None,
                null=True,
                upload_to="csv/%Y/%m/%d/",
                verbose_name="CSV файл",
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="cancel_dt",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Дата когда закончилось",
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="created_at",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Дата создания"
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="date",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Дата продажи"
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="discount_percent",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Процент скидки"
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="is_cancel",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Закончилось на складе",
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="last_change_date",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Дата последней продажи",
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="nm_id",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Продукт ID"
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="total_price",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Сумма"
            ),
        ),
        migrations.AlterField(
            model_name="googletab",
            name="updated_at",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Дата изменения"
            ),
        ),
    ]
