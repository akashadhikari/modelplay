from django.db import models

from client.models import Client
from communication.models import Communication


CLIENT_VALUES = (
    ('High', 'High'),
    ('Mid', 'Mid'),
    ('Low', 'Low'),
)

# LeadPost deals with stuff such as Top Job post, Hot job post or anything customizable


class LeadPost(models.Model):

    post = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.post)

# Keeps track of lead stages which can be customly defined

class LeadStage(models.Model):

    stage = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.stage)

# LG1 Generate Lead Form

class Lead(models.Model):

    employer_name = models.CharField(max_length=255, blank=False)
    post_type = models.ForeignKey(LeadPost, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False)

    # Display Client Basic Info

    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    client_value = models.CharField(max_length=15, choices=CLIENT_VALUES)

    def __str__(self):
        return "{} with {}".format(self.client, self.post_type)

# Lead name and lead stage track

class SalesLead(models.Model):
    
    lead_name = models.ForeignKey(Lead, on_delete=models.CASCADE) #Active list of lead
    lead_stage = models.ForeignKey(LeadStage, on_delete=models.CASCADE)
    communication = models.ForeignKey(Communication, on_delete=models.CASCADE)

    def __str__(self):
        return "{} at {}".format(self.lead_name, self.lead_stage)

