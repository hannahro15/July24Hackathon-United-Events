from django.db import models


class Event(models.Model):
    """
    Model for handling the pride events around the UK.
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    highlights = models.TextField(null=False, blank=False)
    accessibility = models.TextField(null=True, blank=True)
    ticket_info = models.TextField(null=False, blank=False)
    additional_notes = models.TextField(null=True, blank=True)
    website = models.URLField()

    class Meta:
        ordering = ["start_date", "location", "name"]

    def __str__(self):
        return self.name
