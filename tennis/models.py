from django.db import models


class ContactForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.first_name
