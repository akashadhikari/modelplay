from django.db import models


class Client(models.Model):

    name = models.CharField(max_length=255, blank=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
