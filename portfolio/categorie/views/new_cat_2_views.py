from categorie.forms import NewCategorieNiv2
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required


@login_required
def new_cat_deux(request):
    """
    create a new category of level 2
    :param request: environement variable
    :return: template with a form
    """
    form_ncn_2 = NewCategorieNiv2(request.POST or None)
    if form_ncn_2.is_valid():
        form_ncn_2.save()
        return redirect(reverse('accueil'))
    context = {'form_cat_niv_2': form_ncn_2}
    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)