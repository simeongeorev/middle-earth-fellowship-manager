from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Fellowship(models.Model):
    name = models.CharField(max_length=50, unique=True)

    leader_name = models.CharField(max_length=50)

    formation_date = models.DateField(default=date.today)

    origin_realm = models.CharField(max_length=100)

    max_members = models.IntegerField(validators=[
        MinValueValidator(2),
        MaxValueValidator(12)
    ])

    is_active = models.BooleanField(default=False)

    def update_status(self):
        self.is_active = self.quests.count() > 0
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-formation_date']

