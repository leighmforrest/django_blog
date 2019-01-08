from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'{self.title}: {self.content[:100]}'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
