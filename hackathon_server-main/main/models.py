from django.db import models

class Post(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank=True, null=True, upload_to="images/")
    contents = models.TextField()

    def __str__(self):
        return self.postname
