from __future__ import unicode_literals
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils import timezone


# Create your models here.

class Suggestion(TimeStampedModel, models.Model):
    description = models.TextField()

    def __str__(self):
        return str(self.id)


from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Suggestion)
def email_suggestion(sender, instance, **kwargs):
    """Upon saving a suggestion, email our CEO."""

    body = """
    Hello, Sharon ---

    There is a new suggestion!

    %s

    Thank you,
    Cheerful Staff Robot
    """ % instance.description

    send_mail("New suggestion",
              body,
              "joel@joelburton.com",
              ["sharon@hackbrightacademy.com"])
