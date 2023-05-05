from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class ProjectDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    project_dec = models.TextField()
    technology_used = models.CharField(max_length=500)
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProjectDetails, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImages(models.Model):
    project = models.ForeignKey(ProjectDetails,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='E-playhere/projectImg',null=True,blank=True)