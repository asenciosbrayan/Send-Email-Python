import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

remitente = '' #CORREO ENCARGADO DE ENVIAR EL MENSAJE
destinatarios = ['',''] #CORREOS A ENVIAR
asunto = '' #ASUNTO DEL CORREO
cuerpo = '' #CUERPO DEL CORREO

ruta = '' #RUTA DEL ARCHIVO A ENVIAR EN EL CORREO
archive_name = [] #NOMBRE DEL ARCHIVO
formato = '' #FORMATO DEL ARCHIVO

for i in range(23):
    sumarutasdecla = ruta+'/'+archive_name[i]+formato 

    ruta_adjunto = sumarutasdecla 

    nombre_adjunto = archive_name[i]+formato 

    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatarios[i]
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    archivo_adjunto = open(ruta_adjunto, 'rb')
    
    adjunto_MIME = MIMEBase('application', 'octet-stream')

    adjunto_MIME.set_payload((archivo_adjunto).read())

    encoders.encode_base64(adjunto_MIME)

    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)

    mensaje.attach(adjunto_MIME)
    
    sesion_smtp = smtplib.SMTP('smtp.outlook.com', 587)
    
    sesion_smtp.starttls()

    sesion_smtp.login('#CORREO-REMITENTE','#PASSWORD-CORREO-REMITENTE')

    texto = mensaje.as_string()

    sesion_smtp.sendmail(remitente, destinatarios[i], texto)

    sesion_smtp.quit()
    print("ENVIADO A:", archive_name[i] , "/" , destinatarios[i])