from datetime import date

from django.core.exceptions import ValidationError
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

    def clean(self):
        super().clean()
        current_members_count = self.characters.count()
        if self.max_members < current_members_count:
            raise ValidationError({
                'max_members': f"This fellowship already has {current_members_count} members."
                               f"The maximum cannot be lower than that."
            })

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-formation_date']

