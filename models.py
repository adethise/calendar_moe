from django.db import models

class DateEntry(models.Model):
    date   = models.ForeignKey('Date')
    source = models.CharField(max_length = 512)
    image  = models.ImageField(upload_to='uploads/dates/')

    def __str__(self):
        return 'Entry from %s for date %s' % (self.source, self.date)


class Date(models.Model):
    day   = models.IntegerField()
    month = models.IntegerField()

    def __str__(self):
        return '%d-%d' % (self.month, self.day)
