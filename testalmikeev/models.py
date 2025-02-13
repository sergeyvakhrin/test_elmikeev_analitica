from django.db import models


NULLABLE = {"null": True, "blank": True}


class GoogleTab(models.Model):
    """ Класс для загрузки данных из гугл таблицы """
    date = models.CharField(max_length=50, verbose_name='Дата продажи', **NULLABLE)
    last_change_date = models.CharField(max_length=50, verbose_name='Дата последней продажи', **NULLABLE)
    total_price = models.FloatField(verbose_name='Сумма', **NULLABLE)
    discount_percent = models.CharField(max_length=50, verbose_name='Процент скидки', **NULLABLE)
    warehouse_name = models.CharField(max_length=50, verbose_name='Название склада', **NULLABLE)
    oblast = models.CharField(max_length=50, verbose_name='Область РФ', **NULLABLE)
    nm_id = models.CharField(max_length=50, verbose_name='Продукт ID', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='Категория', **NULLABLE)
    brand = models.CharField(max_length=50, verbose_name='Бренд', **NULLABLE)
    is_cancel = models.CharField(max_length=50, verbose_name='Закончилось на складе', **NULLABLE)
    cancel_dt = models.CharField(max_length=50, verbose_name='Дата когда закончилось', **NULLABLE)
    created_at = models.CharField(max_length=50, verbose_name="Дата создания", **NULLABLE)
    updated_at = models.CharField(max_length=50, verbose_name="Дата изменения", **NULLABLE)
    order_type = models.CharField(max_length=50, verbose_name='Тип продажи', **NULLABLE)

    # def __str__(self):
    #     return self.nm_id

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class FileCsv(models.Model):
    file = models.FileField(upload_to='csv/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name="CSV файл")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


class Report(models.Model):
    nm_id = models.CharField(max_length=50, verbose_name='Продукт ID', **NULLABLE)
    report = models.FloatField(verbose_name='Сумма', **NULLABLE)

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"

    def __str__(self):
        return self.nm_id
