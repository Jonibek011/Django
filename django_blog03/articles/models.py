from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
