from django.db import models

# Create your models here.


class Entity(models.Model):
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.content
