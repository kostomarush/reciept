from django.shortcuts import render, redirect

from .models import Recipe, RecipeIngredient, AuthorProfile





def main(request): #Открытие окна кулимнарных книг
    
    all_info = RecipeIngredient.objects.all()

    data = {

            'all_info': all_info, # Данные из БД для вывода в html форму, аналогично остальные функции

    }
    
    return render(request, 'server/main.html', data)

def open(request, pk): # Описание рецептов

    recipe = RecipeIngredient.objects.get(pk=pk)
    data = {
        'recipe': recipe,
    }
    
    return render(request, 'server/open.html', data)

def auth(request):# Откртыие окна с авторами

    auth = AuthorProfile.objects.all()
    data = {
        'auth': auth,
    }
    
    return render(request, 'server/authors.html', data)