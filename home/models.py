from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Image(models.Model):
    image = models.ImageField(upload_to='home')
    desc = models.TextField()
    link_text = models.CharField(max_length=50, blank=True, null=True)
    link = models.CharField(max_length=50, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.desc


@receiver(post_save, sender=Image)
def set_default_order(sender, instance, created, **kwargs):
    if created and instance.order is None:
        # Temporarily disconnect the signal to avoid an infinite loop (the created variable should prevent this, but it's a good idea to be safe)
        post_save.disconnect(set_default_order, sender=Image)

        instance.order = 100 * instance.pk
        instance.save()

        # Reconnect the signal
        post_save.connect(set_default_order, sender=Image)
