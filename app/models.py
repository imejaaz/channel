from django.db import models

# Create your models here.

class group(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class messages(models.Model):
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    time = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content