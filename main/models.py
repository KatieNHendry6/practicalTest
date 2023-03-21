from django.db import models

class page(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128, default='name name')
    date = models.DateField(max_length=0, null=True)
    description = models.TextField(default='a sentence')

    def __str__(self):
            return self.title
