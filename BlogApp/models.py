from django.db import models
from django.utils.timezone import now
from django.utils.timezone import utc
import datetime
class Blog(models.Model):
    title = models.CharField(max_length = 30, default = 'GARCHIG') 
    shortNews = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200, null = True)
    news = models.TextField()
    createdDate = models.DateTimeField(default=now, blank= True)
    author = models.CharField(max_length = 30)
    image = models.URLField()
    def __str__(self):
        return self.title
    @property
    def timeDiff(self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        timediff = now - self.createdDate
        totalSec = int(timediff.total_seconds())
        return str(totalSec//60) + ' мин ' + str(totalSec%60)  + ' сек'

    class Meta():
        db_table = 'news'

class Chart(models.Model):
    Monday  = models.IntegerField()
    Tuesday  = models.IntegerField()
    Wednesday  = models.IntegerField()
    Thursday  = models.IntegerField()
    Friday  = models.IntegerField()
    Saturday = models.IntegerField()
    Sunday = models.IntegerField()
    class Meta():
        db_table = 'chart'