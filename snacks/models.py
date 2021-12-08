from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    purchaser = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)

    def get_absolute_url(self):
        return reverse('snack_detail', args=[self.id])

    def __str__(self):
        return str(self.title)

