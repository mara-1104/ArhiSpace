from django.db import models

# Create your models here.

class EstimarePret(models.Model):
    suprafata = models.FloatField()
    rezultat = models.FloatField()
    plan = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.suprafata} m² - {self.plan} - {self.rezultat} €"
