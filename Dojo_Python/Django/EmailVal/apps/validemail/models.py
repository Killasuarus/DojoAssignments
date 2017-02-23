from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class EmailManager(models.Manager):
    def add_email(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            return {'status':False, 'errors':"Not a valid email address"}
        else:
            newemail = self.create(email=postData['email'])
            print newemail
            return {'status':True}
class Email(models.Model):
    email = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EmailManager()

# class EmailManager(models.Manager):
#     def add(self, postData):
#
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(postData['email']):
#             return {'status':False, 'errors':'Not a valid email address'}
#         else:
#             newemail = self.create(email=postData['email'])
#             return {'status':True}, newemail
