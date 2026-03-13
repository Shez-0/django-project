from django.db import models

# Create your models here.

class Blackjack(models.Model):
    player_score = models.IntegerField()
    dealer_score = models.IntegerField()
    player_bet = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=20)
    balance = models.IntegerField()

class Slots(models.Model):
    player_bet = models.IntegerField()

class Roulette(models.Model):
    player_bet = models.IntegerField()
    player_number = models.IntegerField()
    player_color = models.CharField(max_length=5)
