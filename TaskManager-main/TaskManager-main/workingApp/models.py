from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# table for storing lists
class TaskList(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(default=timezone.now) # if we write default = timezone.now() the timezone function gets called and it takes the time when the migrations are run.  instead use timezone.now which gets called at the object creation
	deadline = models.DateField(default=timezone.now) # if we write default = timezone.now() the timezone function gets called and it takes the time when the migrations are run.  instead use timezone.now which gets called at the object creation
	completionStatus = models.BooleanField(default=False)
	userKey = models.ForeignKey(User, on_delete= models.CASCADE,  null=True, blank=True)#storing user_id
	def __str__(self):
		return f"{self.name}" 
	class Meta:
		order_with_respect_to = 'userKey'
# drag and drop

# # table for storing tasks
# class Task(models.Model):
# 	name = models.CharField(max_length=50)
# 	desc = models.TextField(null=True, blank=True)
# 	created_at = models.DateTimeField(default=timezone.now) # if we write default = timezone.now() the timezone function gets called and it takes the time when the migrations are run.  instead use timezone.now which gets called at the object creation
# 	completionStatus = models.BooleanField(default=False)
# 	listKey = models.ForeignKey(TaskList, on_delete=models.CASCADE)
# 	def __str__(self):
# 		return f"{self.name}"
