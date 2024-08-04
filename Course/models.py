from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    Title=models.TextField()
    Details=models.TextField()
    def __str__(self):
        return self.Title
    
class enroll_details(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)