from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 35, blank=False, null=False)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    created_at = models.TimeField(auto_now_add=True)
    author = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title
