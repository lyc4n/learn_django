from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    title       = models.CharField(max_length=80)
    description = models.CharField(max_length=300)
    is_done     = models.BooleanField(default=False)
    due_date    = models.DateTimeField('date due_date')
