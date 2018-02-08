from django.db import models


class ContactPerson(models.Model):

    contact_person_name = models.CharField(max_length=255, blank=False)
    designation = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.contact_person_name, self.designation)


class Company(models.Model):

    company_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return"{}".format(self.company_name)


class Client(models.Model):

    group = models.BooleanField(default=False)
    group_of_companies = models.ManyToManyField(Company)
    contact_person = models.ManyToManyField(ContactPerson)
    created = models.DateField(auto_now=True)

    # Secondary Info can be filled likewise

    def __str__(self):
        return "{}".format(self.name)
