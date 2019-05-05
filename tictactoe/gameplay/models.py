from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GAME_STATUS_CHOICES = (
    ('F', 'First player to move'),
    ('S', 'Second player to move'),
    ('W', 'First player wins'),
    ('L', 'Second player wins'),
    ('D', 'Draw'),
)
class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="game_first_player")
    second_player = models.ForeignKey(User, related_name="game_second_player")
    start_time = models.DateField(auto_now_add=True)
    last_active = models.DateField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES) # not specifing default with error when running 'makemigrations'
    ''' You are trying to add a non-nullable field 'status' to game without a default; we can't do that (the database needs something to populate existing rows).
        Please select a fix:
        1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
        2) Quit, and let me add a default in models.py
    '''

    def __str__(self):
        return f"{self.first_player} vs {self.second_player}"

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    # one-to-many relationship between Moves and Game
    game = models.ForeignKey(Game, on_delete=models.CASCADE)