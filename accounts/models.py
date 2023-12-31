
from django.utils.translation import ugettext_lazy as _
from django.utils.http import urlquote
from django.utils import timezone
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=250, unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active Status'), default=True, help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('Join Date'), default=timezone.now)
    
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    class Meta:
        varbose_name = _('user')
        varbose_name_plural = _('users')
        
    def get_absolute_url(self):
        return '/users/%s/' %urlquote(self.email)
    
    def get_full_name(self):
        full_name = '%s %s' %(self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
    
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
    