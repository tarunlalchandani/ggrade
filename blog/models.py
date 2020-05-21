from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


#Create A Blog models
#title
#pub_date
#body
#image

#Add the Blog app to the local_settings

#Create a migration

#Migrate

#Add to the admin
