from __future__ import unicode_literals
from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def register(self, postData):
        # store the possible failed validations
        errors = []
        # first_name length greater than 2
        if len(postData['first_name']) < 2:
            errors.append('First name must be at least 2 characters long!')
        # last_name length greater than 2
        if len(postData['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long!')
        # email cannot be blank
        if not len(postData['email']):
            errors.append('Email field is required')
        # email must be valid
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Email must be valid!')
        # email must be unique
        # password must be at least 8
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters!')
        #passwords must match
        if not postData['password'] == postData['confirm_password']:
            errors.append('Passwords must match!')

        user = self.filter(email = postData['email'])
        # email must be unique
        if user:
            errors.append('Email must be unique')

        modelResponse = {}
        # if failed validations
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = hashed_password)
            modelResponse['status'] = True
            modelResponse['user'] = user
        return modelResponse

    def login(self, postData):
        # check to see if user is in DB
        user = self.filter(email = postData['email'])
        modelResponse = {}
        print user
        # if user exsits
        if user:
            # check for matching passwords
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                # send success to views
                modelResponse['status'] = True
                modelResponse['user'] = user[0]
            # fail match password
            else:
                # send error message to views
                modelResponse['status'] = False
                modelResponse['errors'] = 'Invalid email/password combination'
        else:
            modelResponse['status'] = False
            modelResponse['errors'] = 'Invalid email'

        return modelResponse

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
