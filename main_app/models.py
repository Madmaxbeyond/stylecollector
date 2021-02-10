from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MOODS = (
    ('A', 'fabulous!'),
    ('B', 'okay'),
    ('C', 'not great...')
)


# Create your models here.
class Accessory(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=150)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})   


class Style(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    era = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'style_id': self.id})    
    
    def worn_today(self):
        return self.wearing_set.filter(date=date.today()).count() >= len(MOODS)

class Wearing(models.Model):
    date = models.DateField('wearing date')
    mood = models.CharField(
        max_length=1,
        choices=MOODS,
        default=MOODS[0][0]
    )
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

    def __str__(self):
        return f"Felt {self.get_mood_display()} on {self.date}"

    class Meta:
        ordering = ['-date']