from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class employees(models.Model):
    f_name = models.CharField(max_length=10)
    l_name = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.f_name