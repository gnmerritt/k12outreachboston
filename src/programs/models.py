from django.db import models


class Contact(models.Model):
    """A person we can get in touch with about program(s)"""
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.email)


class Organization(models.Model):
    """Organizations sponsor programs, e.g. Harvard or BU"""
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField()
    site = models.CharField(max_length=200, blank=True)

    age_group = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, blank=True)
    site = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    date = models.CharField(max_length=100, blank=True)
    time = models.CharField(max_length=100, blank=True)

    volunteer_app = models.CharField(max_length=100, blank=True)
    volunteer_app_deadline = models.CharField(max_length=100, blank=True)
    volunteer_time = models.CharField(max_length=100, blank=True)
    volunteer_exp = models.CharField(max_length=100, blank=True)

    student_app = models.CharField(max_length=100, blank=True)
    student_app_deadline = models.CharField(max_length=100, blank=True)

    nomination = models.CharField(max_length=100, blank=True)
    nomination_deadline = models.CharField(max_length=100, blank=True)

    cost = models.CharField(max_length=100)

    scholarship_app = models.CharField(max_length=100, blank=True)
    scholarship_app_deadline = models.CharField(max_length=100, blank=True)

    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)

    donations_accepted = models.BooleanField()
    donations_link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
