from django.db import models

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
    ingredient = models.ManyToManyField(Ingredient, blank=True, null=True)

    def __str__(self):
        return f"Ингридиенты для {self.recipe.title}"
