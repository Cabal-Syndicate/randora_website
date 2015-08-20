from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
  title = models.CharField(max_length=80)
  def __unicode__(self):
    return self.title

class Thread(models.Model):
  title = models.CharField(max_length=80)
  timestamp = models.DateTimeField(auto_now_add=True)
  creator = models.ForeignKey(User, blank=True, null=True)
  board = models.ForeignKey(Board)
  def __unicode__(self):
    return "%s - %s" % (self.title, self.creator)

class Post(models.Model):
  timestamp = models.DateTimeField(auto_now_add=True)
  creator = models.ForeignKey(User, blank=True, null=True)
  thread = models.ForeignKey(Thread)
  body = models.TextField(max_length=10000)
  def __unicode__(self):
    return "%s - %s - %d" % (self.creator, self.thread, self.id)


