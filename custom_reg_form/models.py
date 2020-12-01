from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_noop

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.PROTECT)
    MEMBER_ORGANIZATION_INSTITUTION = (
        ('0', 'No'),
        ('1', 'Yes'),
    )

    org_inst = models.CharField(
        verbose_name=_("Organization/Institution name"),
        blank="True",
        max_length=100,
    )
    tel = models.CharField(
        verbose_name=_("Phone number"),
        max_length=100,
    )
