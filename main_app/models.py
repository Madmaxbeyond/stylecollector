from django.db import models
from django.urls import reverse

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
    

    def __str__(self):
        return self.title
  

class Wearing(models.Model):
    date = models.DateField('Date Worn')
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