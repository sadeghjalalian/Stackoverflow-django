from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=400)
    vote_count = models.IntegerField(default=0)
    views = models.CharField(max_length=1000)
    tags = models.CharField(max_length=300)
    class Meta:
        ordering = ('-vote_count',)

    def __str__(self):
        return self.question