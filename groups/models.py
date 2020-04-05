from django.db import models
from django.contrib.auth import get_user_model

from django.urls import reverse

from django.utils.text import slugify 
import misaka
# Create your models here.

User = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True, editable=False)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='Membership')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    # for the detail view
    def get_absolute_url(self):
        return reverse("groups:detail", kwargs={"slug": self.slug})
    
    # edit metadata
    class Meta:
        ordering = ['name'] #order-by name    


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_groups')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name = 'memberships')
    #* date_joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user') #? makes sure that a user can join a particular group only once