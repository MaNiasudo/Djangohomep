from django.db import models

# Create your models here.


#Contact Models to save data for users that want to contact us
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta: # Meta classes do some action -> read more when needed https://docs.djangoproject.com/en/5.1/ref/models/options/
       ordering = ['created_date']

    def __str__(self):
        return self.name