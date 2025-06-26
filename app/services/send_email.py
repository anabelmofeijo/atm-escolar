import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

class EmailSender:
    def __init__(self, remetente_email, remetente_senha, smtp_servidor="smtp.gmail.com", smtp_porta=587):
        self.remetente_email = remetente_email
        self.remetente_senha = remetente_senha
        self.smtp_servidor = smtp_servidor
        self.smtp_porta = smtp_porta

    def enviar_comprovativo(self, destinatario_email, caminho_pdf):
        
        email = MIMEMultipart()
        email["From"] = self.remetente_email
        email["To"] = destinatario_email
        email["Subject"] = "Comprovativo"
        email.attach(MIMEText("Segue em anexo o comprovativo em PDF.", "plain"))

        try:
            with open(caminho_pdf, "rb") as f:
                pdf = MIMEApplication(f.read(), _subtype="pdf")
                pdf.add_header('Content-Disposition', 'attachment', filename=os.path.basename(caminho_pdf))
                email.attach(pdf)
        except FileNotFoundError:
            print("Arquivo PDF não encontrado.")
            return

        
        try:
            servidor = smtplib.SMTP(self.smtp_servidor, self.smtp_porta)
            servidor.starttls()
            servidor.login(self.remetente_email, self.remetente_senha)
            servidor.sendmail(self.remetente_email, destinatario_email, email.as_string())
            servidor.quit()
            print("E-mail com comprovativo enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
            
            
email = EmailSender(remetente_email="kudipayangola@gmail.com", remetente_senha="wvbp skyq wrxk akjn")