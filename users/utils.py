import random
import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)  # Logger obyektini yaratamiz

def generate_code(length=6):
    """Tasodifiy `length` xonali kod yaratadi"""
    return "".join([str(random.randint(0, 9)) for _ in range(length)])

def send_verification_email(email, code):
    """Email tasdiqlash kodi yuborish"""
    subject = "Email Verification Code"
    message = f"Your verification code is: {code}"
    from_email = settings.DEFAULT_FROM_EMAIL  # `settings.py`dan email olish

    try:
        send_mail(subject, message, from_email, [email], fail_silently=False)
        logger.info(f"Verification email sent to {email}")
    except Exception as e:
        logger.error(f"Failed to send verification email to {email}: {str(e)}")

def send_reset_password_email(email, code):
    """Parolni tiklash kodi yuborish"""
    subject = "Password Reset Code"
    message = f"Your password reset code is: {code}"
    from_email = settings.DEFAULT_FROM_EMAIL  # `settings.py`dan email olish

    try:
        send_mail(subject, message, from_email, [email], fail_silently=False)
        logger.info(f"Password reset email sent to {email}")
    except Exception as e:
        logger.error(f"Failed to send password reset email to {email}: {str(e)}")
