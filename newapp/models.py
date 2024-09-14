from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateField()

    class Meta:
        db_table ='Articles'
    def __str__(self):
        return self.title

class Reference(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='references')
    link = models.CharField(max_length=255)

    class Meta:
        db_table ='References'
    def __str__(self):
        return self.link

class Image(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='images')
    image_path = models.FileField(upload_to="images/")

    class Meta:
        db_table ='Images'
    def __str__(self):
        return self.image_path





