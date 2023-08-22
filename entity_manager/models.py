from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name  


class UniversalEntities(models.Model):
    xtype = models.ForeignKey('Type', on_delete=models.CASCADE)
    xname = models.CharField(max_length=100)
    xdescription = models.TextField(blank=True)
    xcode = models.CharField(max_length=20, blank=True)
    xlatitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    xlongitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    xcreated_at = models.DateTimeField(auto_now_add=True)
    xupdated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.xname
