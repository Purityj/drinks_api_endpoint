from django.db import models

# Create your models here.
# not creating a specif drink here but rather describing what every drink should look like
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
