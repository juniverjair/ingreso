from datetime import datetime
from django.db import models
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from multi_email_field.fields import MultiEmailField
import qrcode
from django.contrib.auth.models import User
from PIL import Image
import random

# Create your models here.


def enviar_correo(asunto, mensaje, destinatarios, qr):
    # Generar codigo QR:

    json = {}
    json["cod"] = qr

    cadena = str(json)
    imagen = qrcode.make(cadena)
    archivo_imagen = open("qr_reunion.png", 'wb')

    imagen.save(archivo_imagen)
    archivo_imagen.close()

    subject = asunto
    message = mensaje
    sender =  'juniver.roman@tia.com.ec'
    recipients = destinatarios

    # cc_myself = form.cleaned_data['cc_myself']
    #
    # if cc_myself:
    #     recipients.append(sender)

    mail = EmailMessage(subject, message, sender, recipients)

    # mail.attach(filename = "acceso.png", mimetype = "image/png", content = imagen)

    mail.attach_file('./qr_reunion.png')
    # mail.attach_file('./ff.ics')

    mail.send(fail_silently=False)

class Sala(models.Model):
    PISOS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    piso = models.CharField(max_length=1, choices=PISOS)
    create_at = models.DateTimeField(default=datetime.now(), editable=False)

    def __str__(self):
        return self.nombre


class Reunion(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=45, null=True)
    correo = MultiEmailField(help_text="A esta lista de email se enviará el QR de acceso, sepárelos mediante ENTER")
    horario = models.DateTimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    activa = models.BooleanField(default=True)
    descripcion = models.TextField(max_length=100)
    create_at = models.DateTimeField(default=datetime.now(), editable=False)
    edited_at = models.DateTimeField(editable=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Reuniones"

    def save(self, *args, **kwargs):
        self.edited_at = datetime.now()
        super().save(*args, **kwargs)

        if self.activa == True:
            asunto = '''ACCESO TIA MATRIZ - REUNION ID ''' + str(self.id)

            mensaje = '''Estimado(a) ''' + self.nombre + ''', el Sistema de Control de Ingreso para proveedores ha generado una reunión para el ''' + str(self.horario.strftime("%Y-%m-%d %H:%M:%S")) + ''' en el sala ''' + str(self.sala) + '''. Recuerde llegar a tiempo, caso contrario no podrá ingresar. El código QR adjunto le permitirá su ingreso 10 minutos antes o después de la hora indicada.''' # + str(self.cantidad_personas) + ''' persona(s).'''

            try:
                enviar_correo(asunto, mensaje, self.correo, str(self.id))
            except:
                enviar_correo("ERROR", "SE INFORMA QUE SE PRESENTA UN ERROR EN LA REUNION CON CODIGO " + str(self.id), ["juniver.roman@tia.com.ec"], "test")

class Historial(models.Model):

    id = models.AutoField(primary_key=True)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    ingreso = models.BooleanField(default=True)
    detalle = models.TextField(max_length=300)
    create_at = models.DateTimeField(default=datetime.now(), editable=False)

    def __str__(self):
        return self.reunion.nombre

    class Meta:
        verbose_name_plural = "Historial"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
