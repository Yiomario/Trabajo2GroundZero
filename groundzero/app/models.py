from django.db import models

# Create your models here.

class Arte(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    rut              = models.CharField(max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100)
    direccion        = models.CharField(max_length=50)  
    arte        = models.ForeignKey(Arte, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre
    
opciones_consultas = [
    [0, "Esculturas"],
    [1, "Pinturas"  ],
    [2, "Tejidos"   ],
    [3, "Orfebreria"]
]
class formulario(models.Model):
    rut              = models.CharField(max_length=10)
    edad             = models.CharField(max_length=4)
    nombre           = models.CharField(max_length=20)
    apellidos        = models.CharField(max_length=20)
    correo           = models.EmailField()
    tipo_consulta    = models.IntegerField(choices=opciones_consultas)
    mensaje          = models.TextField()
    avisos           = models.BooleanField()

def __str__(self):
        return self.nombre
    