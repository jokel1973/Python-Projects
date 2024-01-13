from django.db import models



# Create your models here.
class UniversityCampus(models.Model):
    # Attributes
    campus_name = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    # Model manager
    objects = models.Manager()

    # Meta class for admin display
    class Meta:
        verbose_name_plural = 'University Campuses'

    def __str__(self):
        return self.campus_name

