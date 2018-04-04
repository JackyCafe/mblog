from django.db import models

# Create your models
from django.utils import timezone


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title  = models.CharField(max_length=200)
    slug  = models.CharField(max_length=200)
    content = models.TextField( )
    owner = models.CharField(max_length=200)
    pub_date = models.DateField(default= timezone.now)

    class Meta:
        ordering = ('-pub_date',)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title.encode('utf-8')

    def decade_date(self):
        datestr =  self.pub_date.strftime('%Y/%m/%d')
        return datestr