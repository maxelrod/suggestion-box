from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class Recipient(models.Model):
    """Potential recipient."""

    name = models.CharField(
        max_length=30,
    )

    email = models.EmailField(
        max_length=30,
    )

    def __str__(self):
        return str(self.name)


class Suggestion(TimeStampedModel, StatusModel, models.Model):
    """A suggestion in the suggestion box."""

    STATUS = [('new', 'New'), ('in-process', 'In-Process'), ('closed', 'Closed')]

    suggestion = models.TextField()

    recipient = models.ForeignKey(
        Recipient
    )

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=Suggestion)
def email_suggestion(sender, instance, **kwargs):
    """Upon saving a suggestion, email our CEO."""

    body = """
    Hello %s ---

    There is a new suggestion!


    %s


    Thank you,
    Cheerful Staff Robot
    """ % (instance.recipient.name, instance.suggestion)

    send_mail("New suggestion",
              body,
              "joel@joelburton.com",
              [instance.recipient.email])
