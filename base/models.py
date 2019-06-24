from django.db import models
from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    source_url = models.CharField(max_length=300)
    emb_link = models.CharField(max_length=300)
    content = models.TextField(blank=True, null=True)
    
