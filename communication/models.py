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

class ContactPerson(models.Model):

    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "{}".format(self.name)

MEDIUMS = (
    ('Outbound Call', 'Outbound Call'),
    ('Inbound Call', 'Inbound Call'),
    ('Inbound Email', 'Inbound Email'),
    ('Outbound Email', 'Outbound Email'),
    ('SMS', 'SMS'),
    ('Meeting', 'Meeting')
)


class Communication(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100, choices=MEDIUMS)
    sales_stage = models.ForeignKey(SubStage, on_delete=models.CASCADE)
    set_reminder= models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    fields = JSONField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} is contacted by {} through {} at {} on {}"\
            .format(self.client, self.contact_person, self.medium, self.sales_stage, self.created)