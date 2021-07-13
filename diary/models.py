from django.db import models

# Create your models here.
class Diary(models.Model) :
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField()
    weather = models.CharField(max_length=50)

    def __str__(self) :
        return self.image