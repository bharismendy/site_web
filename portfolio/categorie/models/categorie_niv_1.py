from django.db import models


class CategorieNiv1(models.Model):
    """this class is use to categorise every article"""
    nom_categorie = models.CharField(max_length=100, default=None, null=False)
    has_sub = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_categorie
