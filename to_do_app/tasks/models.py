from django.db import models

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length = 500)
    complete = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.task_name
    