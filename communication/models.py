from django.db import models
from django.contrib.postgres.fields import JSONField

from client.models import Client, ContactPerson

# SalesGroup, in this case has Suspecting, Prospecting, Approaching, Negotiation


class SalesGroup(models.Model):

    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.name)


# Each SubStage belongs to a certain SalesGroup


class SubStage(models.Model):

    sales_group = models.ForeignKey(SalesGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    # enable date
    # enable remarks
    # enable any data type
    # set_reminder= models.DateTimeField(null=True, blank=True)
    # remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} > {}".format(self.sales_group, self.name)


MEDIUMS = (
    ('Outbound Call', 'Outbound Call'),
    ('Inbound Call', 'Inbound Call'),
    ('Inbound Email', 'Inbound Email'),
    ('Outbound Email', 'Outbound Email'),
    ('SMS', 'SMS'),
    ('Meeting', 'Meeting')
)

MEDIUM_DIRECTION = (
    ('Inbound', 'Inbound'),
    ('Outbound', 'Outbound'),
)

MEDIUM_STATUS = (
    ('Successful', 'Successful'),
    ('Unsuccessful', 'Unsuccessful'),
)


class Communication(models.Model):

    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100, choices=MEDIUMS)
    medium_direction = models.CharField(max_length=100, choices=MEDIUM_DIRECTION)
    medium_status = models.CharField(max_length=100, choices=MEDIUM_STATUS)
    sales_stage = models.ForeignKey(SubStage, on_delete=models.CASCADE)

    # fields = JSONField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} is contacted by {} through {} at {} on {}"\
            .format(self.lead_name, self.contact_person, self.medium, self.sales_stage, self.created)

