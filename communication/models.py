from django.db import models
from django.contrib.postgres.fields import JSONField

from client.models import Client

# SalesGroup, in this case has Suspecting, Prospecting, Approaching, Negotiation


class SalesGroup(models.Model):

    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.name)


# Each SubStage belongs to a certain SalesGroup


class SubStage(models.Model):

    sales_group = models.ForeignKey(SalesGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{} > {}".format(self.sales_group, self.name)


class Communication(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sales_stage = models.ForeignKey(SubStage, on_delete=models.CASCADE)
    fields = JSONField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return "{} is contacted by {} at {} on {}"\
            .format(self.client, self.contact, self.sales_stage, self.created)