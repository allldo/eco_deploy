from django.db import models


class Project(models.Model):

    name = models.TextField(max_length=65)

    def __str__(self):
        return self.name
