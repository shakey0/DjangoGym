from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    DOB = models.DateField()
    image = models.ImageField(upload_to='instructors')
    entry_code = models.CharField(max_length=10)
    instr_type = models.CharField(max_length=50)
    desc = models.TextField()
    qualifications = models.JSONField()
    activities = models.JSONField()
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Instructor)
def set_default_order(sender, instance, created, **kwargs):
    if created and instance.order is None:
        # Temporarily disconnect the signal to avoid an infinite loop (the created variable should prevent this, but it's a good idea to be safe)
        post_save.disconnect(set_default_order, sender=Instructor)

        instance.order = 100 * instance.pk
        instance.save()

        # Reconnect the signal
        post_save.connect(set_default_order, sender=Instructor)
