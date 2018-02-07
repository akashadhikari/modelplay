from django.db import models

from client.models import Client
from communication.models import Communication


class LeadPost(models.Model):

    post = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.post)


class LeadStage(models.Model):

    stage = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.stage)


class Lead(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    communication = models.ForeignKey(Communication, on_delete=models.CASCADE)
    lead_stage = models.ForeignKey(LeadStage, on_delete=models.CASCADE)
    lead_post = models.ForeignKey(LeadPost, on_delete=models.CASCADE)

    def __str__(self):
        return "{} at {}".format(self.client, self.lead_stage)