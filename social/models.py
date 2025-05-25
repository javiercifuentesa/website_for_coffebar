from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name= "Key name", max_length=100, primary_key=True)
    name = models.CharField(verbose_name="Social media", max_length=100)
    url = models.URLField(verbose_name="URL", max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ['name']

    def __str__(self):
        return self.name