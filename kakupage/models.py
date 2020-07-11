from django.db import models

# Create your models here.


class Contactus(models.Model):
    name = models.CharField(max_length=50, blank=True)
    sender = models.EmailField(blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact Us"

    # def kakucontact(self):
    #     return self.Meta
