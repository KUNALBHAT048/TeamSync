from django.db import models
from django.contrib.auth.models import User

class ProjectList(models.Model):
   fkey = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length = 100)
   status =  models.BooleanField(default = False)
   name1 = models.CharField(max_length = 100 , null = True)

   @property   
   def CreaterID(self):
       return self.fkey.userId
  
   def ProjectContributors(self):
       return self.fkey.userId
  
   def __str__(self):
       return self.name1


class Project_History(models.Model):
   contributorId = models.ForeignKey(User, on_delete=models.CASCADE)
   project_name = models.CharField(max_length=255)
   description = models.TextField()


   def __str__(self):
       return self.project_name


class Chat(models.Model):
   fkey = models.ForeignKey(User, on_delete=models.CASCADE)
   chatId = models.CharField(max_length = 10)
   message = models.CharField(max_length = 1000, null = True)


   @property
   def senderId(self):
       return self.fkey.userId
   def recieverID(self):
       return self.fkey.userId