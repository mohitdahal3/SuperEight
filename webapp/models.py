from django.db import models

# Create your models here.
class Row(models.Model):
    column1 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column2 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column3 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column4 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column5 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column6 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column7 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column8 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column9 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column10 = models.CharField(max_length=100 , blank=True , null=True , default="")

    def __str__(self):
        return "Row"
