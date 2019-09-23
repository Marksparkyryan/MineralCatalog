from collections import OrderedDict
from django.db import models


class Mineral(models.Model):
    """mineral model describing attributes of each mineral instance"""
    name = models.CharField(max_length=256, unique=True)
    image_filename = models.CharField(max_length=256)
    image_caption = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    formula = models.CharField(max_length=256)
    strunz_classification = models.CharField(max_length=256)
    crystal_system = models.CharField(max_length=256)
    unit_cell = models.TextField(max_length=528)
    color = models.CharField(max_length=256)
    crystal_symmetry = models.CharField(max_length=256)
    cleavage = models.CharField(max_length=256)
    mohs_scale_hardness = models.CharField(max_length=256)
    luster = models.CharField(max_length=256)
    streak = models.CharField(max_length=256)
    diaphaneity = models.CharField(max_length=256)
    group = models.CharField(max_length=256)
    optical_properties = models.CharField(max_length=256)
    refractive_index = models.CharField(max_length=256)
    crystal_habit = models.CharField(max_length=256)
    specific_gravity = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    @property
    def fields_lower(self):
        """retrieve all fields on instance, strip out underscores in 
        field name (meta fields have underscores), then return a list of 
        all these cleaned field names
        """  
        cleaned_fields = {}
        for field in self._meta.fields:
            if field.value_to_string(self):
                without_underscores = field.name.replace("_", " ")
                cleaned_fields.update(
                    {without_underscores: field.value_to_string(self)}
                )
        return cleaned_fields

    @property
    def fields_capitalized(self):
        """retrieve all fields on instance, capitalize all words in 
        field name, then return a list of all these cleaned field names
        """
        cleaned_fields = {}
        for field in self._meta.fields:
            if field.value_to_string(self):
                without_underscores = field.name.replace("_", " ")
                capitalized = " ".join(
                    [x.capitalize() for x in without_underscores.split()]
                )
                cleaned_fields.update(
                    {capitalized: field.value_to_string(self)}
                )
        return cleaned_fields
