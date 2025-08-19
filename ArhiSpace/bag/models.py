from django.db import models

class BagEntry(models.Model):
    plan = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plan} - {self.email}"