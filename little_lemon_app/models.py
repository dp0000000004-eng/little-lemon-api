from django.db import models

# Create your models here.

class Catagory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name="catagory")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.catagory}"