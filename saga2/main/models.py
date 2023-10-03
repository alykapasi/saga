from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# CHOICES = [
#     (1, 'Alice in Wonderland'),
#     (2, 'Beauty and the Beast'),
#     (3, 'Christmas Carol'),
#     (4, 'Cinderella'),
#     (5, 'Snow White and the Seven Dwarfs'),
#     (6, 'Little Red Riding Hood'),
#     (7, 'Sleeping Beauty'),
#     (8, 'Rapunzel'),
#     (9, 'Rumplestiltskin'),
#     (10, 'Jack and the Beanstalk'),
#     (11, 'The Legend of the Sleepy Hollow'),
#     (12, 'Peter Pan'),
#     (13, 'Phantom of the Opera'),
#     (14, 'Winnie the Pooh'),
#     (15, 'The Wizard of Oz'),
#     (16, 'Treasure Island'),
#     (17, 'The Little Mermaid'),
#     (18, 'The Ugly Duckling'),
#     (19, 'Thumbelina'),
#     (20, 'Hansel and Gretel'),
#     (21, 'The Emperor\'s New Suit'),
#     (22, 'Puss in Boots'),
#     (23, 'Goldilocks'),
#     ]


# class Story(models.Model):
#     story_id = models.IntegerField(choices=CHOICES)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories', default=1)
#     # curr_point = models.IntegerField()

# class UserPrompts(models.Model):
#     story = models.ForeignKey(Story, on_delete=models.PROTECT)
#     prompt = models.TextField()

# class AiResponses(models.Model):
#     prompt = models.OneToOneField(UserPrompts, on_delete=models.PROTECT)
#     response = models.TextField()

class ChatSession(models.Model):
    session_id = models.CharField(max_length=128, unique=True)

class ChatMessage(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    content = models.TextField()
    role = models.CharField(max_length=10) # 'user' or 'assistant'
    timestamp = models.DateTimeField(auto_now_add=True)