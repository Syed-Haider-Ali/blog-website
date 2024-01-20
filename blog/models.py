from django.db import models
from user_management.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=800)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING ,related_name='publisher', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING ,related_name="blog_comments", null=True, blank=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING ,related_name='commenter', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# class Image(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING, related_name="blog_images")
#     image = models.ImageField(upload_to="Media")