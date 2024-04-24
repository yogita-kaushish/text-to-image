from django.db import models


# Create your models here.
class Requests(models.Model):
    id = models.AutoField(primary_key=True)
    intercepted_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100,default="Pending", null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}"


class Prompts(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.ForeignKey(Requests, on_delete=models.CASCADE,null=True,blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    response_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}"
