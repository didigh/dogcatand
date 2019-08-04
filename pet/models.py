from django.db import models

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length = 20)
    body = models.TextField()
    date = models.DateTimeField('date published')

    def sum(self):
        return self. body[:2]

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,null=True,related_name='comments')
    contents=models.CharField(max_length=200)

    def __str__(self):
        return self.contents

class Re(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,related_name='replies')
    contents=models.CharField(max_length=200)

    def __str__(self):
        return self.contents