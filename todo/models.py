from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50,verbose_name= "Title")
    completed = models.BooleanField(verbose_name="Status")

    def __str__(self) -> str:
        return self.title
