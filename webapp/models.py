from django.db import models

# Create your models here.
class Member(models.Model):
    id=models.CharField(primary_key=True,max_length=10)
    real_name=models.CharField(max_length=60)
    tz=models.CharField(max_length=60)

    def __unicode__(self):
        return self.real_name
class Activity(models.Model):
    memberid=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='activity_periods')
    start_time=models.CharField(max_length=60)
    end_time=models.CharField(max_length=60)