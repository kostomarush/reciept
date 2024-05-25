from django.db import models

"""
1. У каждой книги несколько рецептов - связь ОДИН КО МНОГИМ

2. У каждого рецепта несколько ингридиентов, а ингридиенты согут использоваться в разынх рецептах - связь МНОГИЕ КО МНОГИМ

3. У каждой книги свой автор - СВЯЗЬ ОДИН К ОДНОМУ

Добавление данных осуществляется через окно Admin в правом верхнем углу

"""

class Cookbook(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class AuthorProfile(models.Model):
    cookbook = models.OneToOneField(Cookbook, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.author_name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient, blank=False)

    def __str__(self):
        return f"Ингридиенты для {self.recipe.title}"
