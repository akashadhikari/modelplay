from django.db import models
from django.contrib.postgres.fields import JSONField


class Client(models.Model):

    name = models.CharField(max_length=255, blank=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class SalesGroup(models.Model):

    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.name)


class SalesStage(models.Model):

    sales_group = models.ForeignKey(SalesGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{} > {}".format(self.sales_group, self.name)


class Communication(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=255, blank=False)
    sales_stage = models.ForeignKey(SalesStage, on_delete=models.CASCADE)
    values = JSONField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return "{} is contacted by {} at {} on {} with values {}"\
            .format(self.client, self.contact_person, self.sales_stage, self.created, self.values)

