from django.db import models
from utilisateur.models import Personne
from markdownx.models import MarkdownxField


class Article (models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    content = MarkdownxField()
    # Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="image_projet/")

    def __str__(self):
        return "article de " + self.personne.user.username
