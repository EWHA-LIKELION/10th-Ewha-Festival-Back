from django.db import models
from account.models import User


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Day(models.Model):
    DAY_CHOICES = (
        ('수요일', '수요일'),
        ('목요일', '목요일'),
        ('금요일', '금요일'),
    )
    DATE_CHOICES = (
        (14, 14),
        (15, 15),
        (16, 16),
    )

    day = models.CharField(choices=DAY_CHOICES, max_length=5)
    date = models.IntegerField(choices=DATE_CHOICES)

    def __str__(self):
        return f'{self.day}'


class Booth(TimeStamp):
    COLLEGE_CHOICES = (
        ('학관', '학관'),
        ('포스코관', '포스코관'),
        ('경영관', '경영관'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ManyToManyField(Day, related_name='booths')
    college = models.CharField(choices=COLLEGE_CHOICES, max_length=20)
    name = models.TextField()
    number = models.CharField(max_length=10, blank=True)
    image = models.URLField(blank=True)
    notice = models.TextField(blank=True)
    description = models.TextField(blank=True)
    like = models.ManyToManyField(User, related_name='booths', blank=True)

    def __str__(self):
        return self.name


class Menu(TimeStamp):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='menus')
    menu = models.TextField()
    image = models.URLField(blank=True)
    price = models.PositiveIntegerField()
    is_soldout = models.BooleanField(default=False)


class Comment(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE)
    content = models.TextField()

