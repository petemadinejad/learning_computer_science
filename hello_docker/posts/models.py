from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
