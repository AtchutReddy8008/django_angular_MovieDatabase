from django.db import models

# Create your models here.
class Products(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    discription=models.CharField(max_length=100)
    price=models.IntegerField()
    added_date=models.DateField()
    type=models.CharField(max_length=30,choices=(
        ("electronics","electronics"),
        ("kichenware","kichenware"),
        ("clothes","clothes")
    ))