from django.contrib import admin
from .models import AuthorProfile, Cookbook, Ingredient, Recipe, RecipeIngredient

admin.site.register(AuthorProfile)
admin.site.register(Cookbook)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)