from django.db import models
from django.contrib.auth.models import User
from instructor.models import Instructor
from django.db.models.signals import post_save
from django.dispatch import receiver


class Class(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='classes')
    desc = models.TextField()
    instructors = models.ManyToManyField(Instructor, related_name='class_instructors')
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


@receiver(post_save, sender=Class)
def set_default_order(sender, instance, created, **kwargs):
    if created and instance.order is None:
        # Temporarily disconnect the signal to avoid an infinite loop (the created variable should prevent this, but it's a good idea to be safe)
        post_save.disconnect(set_default_order, sender=Class)

        instance.order = 100 * instance.pk
        instance.save()

        # Reconnect the signal
        post_save.connect(set_default_order, sender=Class)
