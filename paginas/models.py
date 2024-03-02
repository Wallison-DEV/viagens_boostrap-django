from django.db import models

# Create your models here.

class Endereco(models.Model):

    rua = models.CharField(max_length = 30)
    numero = models.IntegerField(verbose_name="Número")
    bairro = models.CharField(max_length = 30)
    cidade = models.CharField(max_length = 30)
    referencia = models.CharField(max_length = 30, verbose_name="Referência")

    def __str__(self):
        return "{}({})".format(self.rua, self.cidade)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Campo(models.Model):

    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length = 60)
    cpf = models.CharField(max_length = 14 , unique = True)
    endereco = models.ForeignKey(Endereco, verbose_name=("Endereço"), on_delete=models.PROTECT)

    def __str__(self):
        return "{}({})".format(self.nome, self.cpf)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})