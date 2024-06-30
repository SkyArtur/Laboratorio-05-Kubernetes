from django.db import models


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    sobrenome = models.CharField(max_length=100, verbose_name='Sobrenome')
    nascimento = models.DateField(verbose_name='Nascimento')

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome', 'sobrenome', 'nascimento']
        unique_together = (('nome', 'sobrenome'),)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
