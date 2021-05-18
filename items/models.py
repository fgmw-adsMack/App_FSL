from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from . import constants
import datetime


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Item(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved'),
    )
    TYPE_CHOICES = (
        ('book', 'Book'),
        ('movie', 'Movie'),
        ('series', 'Series'),
    )
    item_type = models.CharField(max_length=6, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    year = models.IntegerField(validators=[MinValueValidator(1800),
                                           max_value_current_year])
    country = models.CharField(max_length=55,
                               choices=constants.COUNTRIES_CHOICES)
    author = models.CharField(max_length=255, null=True)
    publisher = models.CharField(max_length=255, null=True)
    director = models.CharField(max_length=255, null=True)
    cast = models.CharField(max_length=255, null=True)
    seasons = models.IntegerField(validators=[MinValueValidator(1),
                                              MaxValueValidator(50)], null=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES,
                              default='pending')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Evaluation(models.Model):
    CHOICES = [(i,i) for i in range(11)]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='evaluations')
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='evaluations')
    rating = models.IntegerField(
        validators=[MinValueValidator(0),
        MaxValueValidator(10)],
        choices=CHOICES)
    comment = models.CharField(max_length=255,blank=True,default='')
    #####
    # total_likes = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User,related_name='likes')
    #####
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['item']

    def __str__(self):
        return f"{self.user} rated ~> {self.item}"

# class Like(models.Model):

#     user = models.ForeignKey(
#         User, 
#         on_delete=models.CASCADE, 
#         related_name='likes')
#     evaluation = models.ForeignKey(
#         Evaluation, 
#         on_delete=models.CASCADE, 
#         related_name='likes')
    
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['user', 'evaluation'], name="unique_like"),
#         ]
    
#     def __str__(self):
#         return f"{self.user} liked ~> {self.evaluation}"