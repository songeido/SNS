from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now = True)
    snsimage = models.ImageField(upload_to = '')
    good = models.IntegerField(null=True,blank=True,default=0)
    read = models.IntegerField(null=True,blank=True,default=0)
    readtext = models.TextField(null=True,blank=True,default=" ")

    def __str__(self):
        return self.title

