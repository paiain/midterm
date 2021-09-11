from django.db import models

# Create your models here.
from django.db import models

SKILL = [
    (1, 'a'),
    (2, 'b'),
    (3, 'c'),
    (4, 'd'),
]


class Doctor(models.Model):
    """Model definition for Doctor."""

    # TODO: Define fields here
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    skill = models.IntegerField(choices=SKILL)

    class Meta:
        """Meta definition for Doctor."""

        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        """Unicode representation of Doctor."""
        return self.first_name+''+self.last_name
