from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE, SET_NULL


# Create your models here.
class Character(models.Model):
    class Specializations(models.TextChoices):
        WIZARD = 'Wizard', 'Wizard'
        WARRIOR = 'Warrior', 'Warrior'
        ARCHER = 'Archer', 'Archer'
        ROGUE = 'Rogue', 'Rogue'
        SUPPORT = 'Support', 'Support'

    class Races(models.TextChoices):
        HUMAN = 'Human', 'Human'
        ELF = 'Elf', 'Elf'
        HOBBIT = 'Hobbit', 'Hobbit'
        ORC = 'Orc', 'Orc'
        OTHER = 'Other', 'Other'

    name = models.CharField(max_length=50)

    image_url = models.URLField()

    race = models.CharField(max_length=20,
                            choices=Races.choices)

    specialization = models.CharField(max_length=20,
                                      choices=Specializations.choices)

    combat_power = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])

    weapon = models.CharField(max_length=50)

    biography = models.TextField(null=True, blank=True)

    fellowship = models.ForeignKey(to='fellowships.Fellowship',
                                   on_delete=SET_NULL,
                                   null=True,
                                   blank=True,
                                   related_name='characters')

    def __str__(self):
        return f"{self.name} ({self.race})"

    class Meta:
        ordering = ['name']