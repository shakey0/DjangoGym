from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='home')
    desc = models.TextField()
    link = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=100)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.desc
