from django.db import models

class TablePsPrice1C(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.CharField(max_length=12)
    id_product = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    sort = models.IntegerField()
    time_update = models.DateTimeField()
    brand = models.CharField(max_length=255)
    brand_clean = models.CharField(max_length=255)
    article = models.CharField(max_length=255)
    article_clean = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_days = models.SmallIntegerField()
    belong = models.CharField(max_length=255)
    code_photo = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=8, decimal_places=3)
    quantity_pack = models.SmallIntegerField()
    control_quantity_pack = models.SmallIntegerField()
    terms_of_sale = models.CharField(max_length=255)
    search = models.TextField()
    cross_articles = models.TextField()
    analogues = models.TextField()
    full_description = models.TextField()
    categories = models.TextField()
    components = models.TextField()
    barcodes = models.TextField()
    suppliers_goods = models.TextField()
    goods_group = models.TextField()
    comments_additional = models.TextField()

    class Meta:
        managed = False
        db_table = 'table_ps_price_1c'

    def __str__(self):
        return self.article + '/' + self.brand
