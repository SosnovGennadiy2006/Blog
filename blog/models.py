from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from users.models import User
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(
        _("Article title"), max_length=250,
        null=False, blank=False
    )
    description = models.TextField(_("Article title"), max_length=500, null=True, blank=False)
    body = RichTextField(_("Article content"))
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['-time_create']
        indexes = [models.Index(fields=['-time_create'])]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])