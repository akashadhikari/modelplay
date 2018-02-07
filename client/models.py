from django.db import models
from django.contrib.postgres.fields import JSONField


class Client(models.Model):

    name = models.CharField(max_length=255, blank=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


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
    contact_person = models.CharField(max_length=255, blank=False)
    sales_stage = models.ForeignKey(SubStage, on_delete=models.CASCADE)
    fields = JSONField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return "{} is contacted by {} at {} on {}"\
            .format(self.client, self.contact_person, self.sales_stage, self.created)


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
    last_communication = models.ForeignKey(Communication, on_delete=models.CASCADE)
    lead_stage = models.ForeignKey(LeadStage, on_delete=models.CASCADE)

    def __str__(self):
        return "{} at {}".format(self.client, self.lead_stage)
