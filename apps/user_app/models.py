from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def userVal(self, postData):
        results = {'status': True, 'errors': []}
        user = []

        if not postData['first_name'] or len(postData['first_name']) < 3:
            results['status'] = False
            results['errors'].append('Please add a first name with more than 2 characters!')

        if not postData['last_name'] or len(postData['last_name']) < 3:
            results['status'] = False
            results['errors'].append('Please add a last name with more than 2 characters!')

        if not postData['email'] or len(postData['email']) < 4 or not re.match(r"([^@|\s]+@[^@]+\.[^@|\s]+)", postData['email']):
            results['status'] = False
            results['errors'].append('Please add a valid email!')

        if results['status'] == True:
            user = User.objects.filter(email = postData['email'])

        if len(user) != 0:
            results['status'] = False
            results['errors'].append('Information is already in the database please double check everything!')
        return results

    def createUser(self, postData):
        user = User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'])
        return user


class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
