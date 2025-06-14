import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def enviar_email_con_graficos(asunto, cuerpo_texto, figuras, 
                              server, port, sender, password, receiver):
    """
    Envía un correo con gráficos embebidos.
    - figuras: lista de tuplas (matplotlib.figure.Figure, id_cid_str)
    """
    msg = MIMEMultipart('related')
    msg['Subject'] = asunto
    msg['From'] = sender
    msg['To'] = receiver

    # Crear cuerpo HTML con referencias a imágenes cid
    html_body = f"<html><body><p>{cuerpo_texto}</p>"
    for _, cid in figuras:
        html_body += f'<img src="cid:{cid}" style="max-width:100%; height:auto;"><br>'
    html_body += "</body></html>"

    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)

    msg_text = MIMEText(html_body, 'html')
    msg_alternative.attach(msg_text)

    # Adjuntar imágenes de cada figura como MIMEImage
    for fig, cid in figuras:
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        img = MIMEImage(buf.read())
        img.add_header('Content-ID', f'<{cid}>')
        img.add_header('Content-Disposition', 'inline', filename=f'{cid}.png')
        msg.attach(img)
        buf.close()

    # Enviar el correo
    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, msg.as_string())
        print('Correo enviado correctamente.')
    except Exception as e:
        print('Error enviando el correo:', str(e))
