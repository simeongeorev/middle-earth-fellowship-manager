from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Quest(models.Model):
    class Regions(models.TextChoices):
        ERIADOR = "Eriador", "Eriador"
        RHOVANION = "Rhovanion", "Rhovanion"
        GONDOR = "Gondor", "Gondor"
        MORDOR = "Mordor", "Mordor"

    class ThreatLevels(models.TextChoices):
        LOW = "Low", "Low"
        MODERATE = "Moderate", "Moderate"
        SEVERE = "Severe", "Severe"

    title = models.CharField(max_length=100)

    region = models.CharField(max_length=20,
                              choices=Regions.choices)

    threat_level = models.CharField(max_length=20,
                                    choices=ThreatLevels.choices)

    reward_gold = models.PositiveIntegerField()

    assigned_fellowships = models.ManyToManyField(to='fellowships.Fellowship',
                                                  related_name='quests',
                                                  blank=True)

    def __str__(self):
        return f"{self.title} ({self.region})"

    # Mordor cannot have Low threat level
    def clean(self):
        super().clean()
        if self.region == self.Regions.MORDOR and self.threat_level == self.ThreatLevels.LOW:
            raise ValidationError({
                'threat_level': "Quests into Mordor cannot have a Low threat level!"
            })

    class Meta:
        ordering = ['title']
