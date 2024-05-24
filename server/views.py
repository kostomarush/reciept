from django.shortcuts import render, redirect

from .models import Recipe, RecipeIngredient





def main(request):
    
    all_info = RecipeIngredient.objects.all()

    data = {

            'all_info': all_info,

    }
    
    return render(request, 'server/main.html', data)

def open(request, pk):

    recipe = RecipeIngredient.objects.get(pk=pk)
    data = {
        'recipe': recipe,
    }
    
    return render(request, 'server/open.html', data)