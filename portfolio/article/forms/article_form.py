from django import forms
from article.models import Article


class EditArticle(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['personne']

    def save(self, commit=True, user=None):
        """
        function to save the article
        with save it and then and then add the category according to thee documentation
        :param commit: do we register the article ?
        :param user: user to associate to the article
        :return: nothing
        """
        art = super(EditArticle, self).save(commit=False)
        art.content = self.cleaned_data['content']
        art.resume = self.cleaned_data['resume']
        art.categorie_niv1 = self.cleaned_data['categorie_niv1'] or None
        art.categorie_niv2 = self.cleaned_data['categorie_niv2'] or None
        art.categorie_niv3 = self.cleaned_data['categorie_niv3'] or None
        art.personne = user
        art.titre = self.cleaned_data['titre']
        if commit and user:
            art.save()
