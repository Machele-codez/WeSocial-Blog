from django.db import models
from groups.models import Group
from django.contrib.auth import get_user_model
import misaka
from django.shortcuts import reverse
# Create your models here.

User = get_user_model()

class Post(models.Model):
    # title = models.CharField(max_length=50, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    content_html = models.TextField(editable=False)
    date_posted = models.DateTimeField(auto_now=True) 
    #ToDo: a post must not necesarily belong to a group
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="posts", blank=True, null=True)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        self.content_html = misaka.html(self.content)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"username": self.user.username, "pk": self.pk})
    
    # change metadata
    class Meta:
        ordering = ['-date_posted'] #? order by most recent first
        unique_together = ('user', 'content')