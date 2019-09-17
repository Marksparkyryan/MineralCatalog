from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=256, default="unknown", unique=True)
    image_filename = models.CharField(max_length=256, default="unknown")
    image_caption = models.CharField(max_length=256, default="unknown")
    category = models.CharField(max_length=256, default="unknown") 
    formula = models.CharField(max_length=256, default="unknown")
    strunz_classification = models.CharField(max_length=256, default="unknown")
    crystal_system = models.CharField(max_length=256, default="unknown")
    unit_cell = models.TextField(max_length=528, default="unknown")
    color = models.CharField(max_length=256, default="unknown")
    crystal_symmetry = models.CharField(max_length=256, default="unknown")
    cleavage = models.CharField(max_length=256, default="unknown")
    mohs_scale_hardness = models.CharField(max_length=256, default="unknown")
    luster = models.CharField(max_length=256, default="unknown")
    streak = models.CharField(max_length=256, default="unknown")
    diaphaneity = models.CharField(max_length=256, default="unknown")
    group = models.CharField(max_length=256, default="unknown")
    optical_properties = models.CharField(max_length=256, default="unknown")
    refractive_index = models.CharField(max_length=256, default="unknown")
    crystal_habit = models.CharField(max_length=256, default="unknown")
    specific_gravity = models.CharField(max_length=256, default="unknown")

    def __str__(self):
        return self.name