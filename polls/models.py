import datetime

from django.db import models
from django.utils import timezone


class Poll(models.Model):
    """ Model to represent attributes and methods of a Poll
    """
    def __unicode__(self):
        """ String representation of a Poll object
        """
        return self.question

    def was_published_recently(self):
        """ Returns True if the Poll was published in < 1 day.
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):

    def __unicode__(self):
        return self.choice_text

    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)