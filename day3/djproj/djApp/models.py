from django.db import models

# Create your models here.


class Track(models.Model):
    track_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.track_name


class Student(models.Model):
    fname = models.CharField(max_length=40, null=True)
    lname = models.CharField(max_length=40, default='noName')
    age = models.IntegerField()
    std_track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False
    is_adult.boolean = True
    is_adult.short_description = 'Graduted'

    def __str__(self):
        return self.fname + " " + self.lname
