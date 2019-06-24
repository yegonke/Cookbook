from django.db import models

# Create your models here.
class Blog(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    source_url = models.CharField(max_length=300)
    emb_link = models.CharField(max_length=300)
    content = models.TextField(blank=True, null=True)
    img_url = models.ImageField(upload_to="web_img", blank=True)
    date_added = models.DateTimeField()
    merits = models.CharField(max_length=300, blank=True)
    demerits = models.CharField(max_length=300, blank=True)
    src_model = models.TextField(blank=True, null=True)
    src_view = models.TextField(blank=True, null=True)
    src_uri = models.TextField(blank=True, null=True)
    forum_url = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'website_blog'
        verbose_name_plural = "Blog"
