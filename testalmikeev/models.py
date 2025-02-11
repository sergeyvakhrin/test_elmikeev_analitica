from django.db import models


NULLABLE = {"null": True, "blank": True}


class GoogleTab(models.Model):
    """ Класс для загрузки данных из гугл таблицы """
    date = models.DateTimeField(verbose_name='Дата продажи', **NULLABLE)
    last_change_date = models.DateField(verbose_name='Дата последней продажи', **NULLABLE)
    total_price = models.PositiveIntegerField(verbose_name='Сумма', **NULLABLE)
    discount_percent = models.SmallIntegerField(verbose_name='Процент скидки', **NULLABLE)
    warehouse_name = models.CharField(max_length=50, verbose_name='Название склада', **NULLABLE)
    oblast = models.CharField(max_length=50, verbose_name='Область РФ', **NULLABLE)
    nm_id = models.IntegerField(verbose_name='Продукт ID', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='Категория', **NULLABLE)
    brand = models.CharField(max_length=50, verbose_name='Бренд', **NULLABLE)
    is_cancel = models.BooleanField(verbose_name='Закончилось на складе', **NULLABLE)
    cancel_dt = models.DateField(verbose_name='Дата когда закончилось', **NULLABLE)
    created_at = models.DateTimeField(verbose_name="Дата создания", **NULLABLE)
    updated_at = models.DateTimeField(verbose_name="Дата изменения", **NULLABLE)
    order_type = models.CharField(max_length=50, verbose_name='Тип продажи', **NULLABLE)

    def __str__(self):
        return self.nm_id

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


