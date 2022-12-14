from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


