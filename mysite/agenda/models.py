from django.db import models
from django.conf import settings
from django.utils import timezone

class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    datum = models.DateField()
    start_tijd = models.TimeField()
    eind_tijd = models.TimeField()
    omschrijving = models.TextField()
    kosten = models.DecimalField(max_digits=10, decimal_places=2)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
