from django.db import models

class PukurBaseModel(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    status      = models.ForeignKey("general.Status", on_delete=models.CASCADE, null=True, blank=True)

    class Meta: abstract = True

class Status(PukurBaseModel):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Fish(PukurBaseModel):
    name        = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Pond(PukurBaseModel):
    name             = models.CharField(max_length=50, unique=True)
    total_water_land = models.DecimalField(max_digits=10, decimal_places=3)
    deepth           = models.DecimalField(max_digits=10, decimal_places=3)
    water_duration   = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name