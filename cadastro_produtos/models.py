from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subcategorias',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE, default=1)  # Default to category with ID 1

    def __str__(self):
        return self.nome
