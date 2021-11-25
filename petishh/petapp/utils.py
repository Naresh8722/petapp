from django.db import models
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib,ssl
from email.message import EmailMessage


class SoftDeleteManager(models.Manager):
	''' Use this manager to get objects that have a isDeleted field '''
	def get_queryset(self):
		return super(SoftDeleteManager, self).get_queryset().filter(is_deleted=False)
	def all_with_deleted(self):
		return super(SoftDeleteManager, self).get_queryset()
	def deleted_set(self):
		return super(SoftDeleteManager, self).get_queryset().filter(is_deleted=True)


class Util:
	@staticmethod
	def send_email(data):
		msg = EmailMessage()
		msg['Subject'] = data['email_subject']
		msg['From'] = "noreply@byhomechefs.com" 
		msg['To'] = data['to_email']
		msg.set_content(data['email_body'])
		s = smtplib.SMTP('byhomechefs.com') 
		s.starttls()
		s.login("noreply@byhomechefs.com","9~^7;Jc?Pksi")
		s.sendmail("noreply@byhomechefs.com", msg['To'], msg.as_string())
	



'''
	def send_email(data):
		email = EmailMessage(
			subject = data['email_subject'],body=data['email_body'], to=[data['to_email']])
		email.send()
	'''