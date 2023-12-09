from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
  name = models.CharField(max_length=200)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Room(models.Model):
  host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200)
  descriptions = models.TextField(null=True, blank=True)
  # participant = 
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-updated', '-created']

  # def __str__ is used to display the name of the room in the admin panel
  def __str__(self):
    return self.name

class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE) # if room is deleted, delete all messages in that room
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.body[0:50] # return first 50 characters of the message body