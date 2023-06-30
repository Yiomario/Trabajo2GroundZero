from django.db import models

# Create your models here.

class Arte(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "Esculturas"],
    [1, "Pinturas"  ],
    [2, "Tejidos"   ],
    [3, "Orfebreria"] 
]
class Producto(models.Model):

    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50 )
    fecha_creacion = models.DateField()  
    precio = models.IntegerField()
    stock = models.IntegerField()  
    arte = models.IntegerField(choices=opciones_consultas)
    descripcion = models.CharField(max_length=42)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre    
    
opciones_consultas = [
    [0, "Esculturas"],
    [1, "Pinturas"  ],
    [2, "Tejidos"   ],
    [3, "Orfebreria"]
]
class Formulario(models.Model):
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


    
