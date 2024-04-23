from django.db import models

class Studente(models.Model):
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)

  def __str__(self):
    return "ID: " + str(self.pk) + ", nome: " + self.name + " " + self.surname

  class Meta:
    verbose_name_plural = "Studenti"

class Insegnamento(models.Model):
  titolo = models.CharField(max_length=50)
  studenti = models.ManyToManyField(Studente, through='Iscrizione', default=None)

  def __str__(self):
    return "ID: " + str(self.pk) + ", materia: " + self.titolo
  
  class Meta:
    verbose_name_plural = "Insegnamenti"

class Iscrizione(models.Model):
    studente = models.ForeignKey(Studente, on_delete=models.CASCADE)
    insegnamento = models.ForeignKey(Insegnamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.studente} iscritto a {self.insegnamento}"
    
    class Meta:
      verbose_name_plural = "Iscrizioni"


