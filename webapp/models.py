from django.db import models


class Row(models.Model):
    column1 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column2 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column3 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column4 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column5 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column6 = models.CharField(max_length=100 , blank=True , null=True , default="")
    column7 = models.CharField(max_length=100 , blank=True , null=True , default="")

    def __str__(self):
        return f"Row"

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150 , blank=True , null=True)
    message = models.TextField(max_length=2000)
    addedDate = models.DateField(verbose_name="Date this was sent" , auto_now_add=True)

    def __str__(self):
        return f"Message by {self.name}"