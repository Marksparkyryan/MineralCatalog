from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse
import re

from .models import Mineral
from .templatetags.mineral_extras import random_mineral


class MineralViewsTest(TestCase):
    """Unit tests for mineral list view and mineral detail view"""

    maxDiff = None

    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name="Abelsonite",
            image_filename="Abelsonite.jpg",
            image_caption="Abelsonite from the Green River Formation, "
            "Uintah County, Utah, US",
            category="Organic",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            strunz_classification="10.CA.20",
            crystal_system="Triclinic",
            unit_cell="a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, "
            "\u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = "
                    "79.99\u00b0Z = 1",
            color="Pink-purple, dark greyish purple, pale purplish red, "
            "reddish brown",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            mohs_scale_hardness="2\u20133",
            luster="Adamantine, sub-metallic",
            streak="Pink",
            diaphaneity="Semitransparent",
            optical_properties="Biaxial",
            group="Organic Minerals",
        )
        self.mineral2 = Mineral.objects.create(
            name="Abernathyite",
            image_filename="Abernathyite.jpg",
            image_caption="Pale yellow abernathyite crystals and green "
            "heinrichite crystals",
            category="Arsenate",
            formula="K(UO<sub>2</sub>)(AsO<sub>4</sub>)\u00b7"
            "<sub>3</sub>H<sub>2</sub>O",
            strunz_classification="08.EB.15",
            crystal_system="Tetragonal",
            unit_cell="a = 7.176\u00c5, c = 18.126\u00c5Z = 4",
            color="Yellow",
            crystal_symmetry="H-M group: 4/m 2/m 2/mSpace group: P4/ncc",
            cleavage="Perfect on {001}",
            mohs_scale_hardness="2.5\u20133",
            luster="Sub-Vitreous, resinous, waxy, greasy",
            streak="Pale yellow",
            diaphaneity="Transparent",
            optical_properties="Uniaxial (-)",
            refractive_index="n\u03c9 = 1.597 \u2013 1.608n\u03b5 = 1.570",
            group="Arsenates",
        )
        self.display_fields = ["category", "formula", "strunz classification",
                               "color", "crystal system", "unit cell",
                               "crystal symmetry", "cleavage",
                               "mohs scale hardness", "luster", "streak",
                               "diaphaneity", "optical properties",
                               "refractive index", "crystal habit",
                               "specific gravity", "group",
                               ]

    def test_mineral_list_view(self):
        """make sure list view is found and rendered"""
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)

    def test_mineral_list_length(self):
        """make sure entire list of minerals is displayed on list view"""
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(len(resp.context['minerals']), 2)

    def test_mineral_title_in_list_html(self):
        """make sure mineral's title is displayed on list view"""
        resp = self.client.get(reverse('minerals:list'))
        self.assertContains(resp, self.mineral1.name)
        self.assertContains(resp, self.mineral2.name)

    def test_valid_letters_in_pagination(self):
        """make sure pagination list contains only valid letters"""
        resp = self.client.get(reverse('minerals:list'))
        pattern = re.compile(r'[a-z]')
        letters = "".join([x for x in resp.context['pagin_list']])
        self.assertRegex(letters, pattern)

    def test_mineral_list_template_used(self):
        """make sure list template is used with list view"""
        resp = self.client.get(reverse('minerals:list'))
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_mineral_detail_view_status(self):
        """make sure detail view is found and rendered"""
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={"pk": self.mineral1.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_mineral_detail_contains_mineral(self):
        """make sure detail view actually contains the intended 
        mineral
        """
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={"pk": self.mineral1.pk}))
        self.assertIsInstance(resp.context['mineral'], Mineral)

    def test_all_mineral_attributes_in_context(self):
        """make sure all attributes from model dict is equal to attributes 
        in context dict
        """
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={"pk": self.mineral1.pk}))
        self.assertDictEqual(self.mineral1.fields_lower,
                             resp.context['fields'])

    def test_available_mineral_attributes_in_html(self):
        """make sure mineral attributes with values are displayed in 
        detail view
        """
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={"pk": self.mineral1.pk}))
        for key, value in self.mineral1.fields_capitalized.items():
            if key.lower() not in ["id", "name", "image filename", "image caption"]:
                self.assertIn(key, resp.content.decode('utf-8'))

    def test_random_mineral_filter(self):
        """make sure random mineral logic returns a good page"""
        resp = self.client.get(
            reverse('minerals:detail',
                    kwargs={
                        "pk": random_mineral([self.mineral1,
                                              self.mineral2]
                                             )
                    }))
        self.assertEqual(resp.status_code, 200)

    def test_mineral_detail_template_used(self):
        """make sure detail template is used for a detail of mineral"""
        resp = self.client.get(
            reverse('minerals:detail',
                    kwargs={"pk": self.mineral1.pk}
                    ))
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    def test_unicode_rendered_in_detail(self):
        """make sure unicode strings are being rendered correctly"""
        resp = self.client.get(
            reverse('minerals:detail',
                    kwargs={"pk": self.mineral1.pk}
                    ))
        self.assertIn(
            "a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, "
            "γ = 79.99°Z = 1",
            resp.content.decode('utf-8'))
