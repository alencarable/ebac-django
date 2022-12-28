from email.policy import default
from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = {
    (0, 'Draft'),
    (1, 'Publish')
}

class Post(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    update_on = models.DateTimeField(auto_now = True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(choices = STATUS, default=0)
    
    object = models.Manager()

    class Meta:
        ordering = ['-created_on'] # ordem decrescente
        #abstract = True # O django não vai criar tabelas a partir dessa classe, e sim das que herdaram da classe Post
    
    def __str__(self):
        return self.title