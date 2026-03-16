from django.db import models

import datetime
from django.utils import timezone

class Pergunta(models.Model):
    titulo = models.CharField(max_length=200, null=False) #texto pequeno obrigatorio
    detalhe = models.TextField(null=False) #texto grande obrigatorio
    tentativa = models.TextField() #texto nao obrigatorio
    data_criacao = models.DateTimeField("Criado em ") #data
    usuario = models.CharField(max_length=200, null=False, default="anônimo") #nome padrão "anônimo"

    def __str__(self): #como se fosse a funçao descrição
        return "[" + str(self.id) + "] " + self.titulo
    
    def foi_publicado_recentemente(self): #perguntas feitas recentemente
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)

    def string_detalhada(self): #infos
        return "id: " + str(self.id) + "; titulo: " + self.titulo + "; detalhe: " + self.detalhe + "; tentativa: " + self.tentativa + "; data criação: " + str(self.data_criacao) + "; usuario: " + self.usuario


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE) #associação da pergunta, pois cada resposta depende de uma pergunta
    # "chave estrangeira" = campo que aponta para uma chave primaria de outra tabela (identificador da pergunta) ex: resposta 15 para a pergunta 15 
    #  on_delete = quando deletar a pergunta, deleta também as respostas associadas a ela
    texto = models.TextField(null=False)
    votos = models.IntegerField(default=0) #campo numero de votos (inteiro)
    data_criacao = models.DateTimeField("Criado em ")
    usuario = models.CharField(max_length=200, null=False, default="anônimo")

    def __str__(self):
        return "[" + str(self.id) + "] " + self.texto
    
    def foi_publicado_recentemente(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)


