from django.conf import settings
from django.db import models

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

    member_org_inst = models.CharField(
        verbose_name="Are you a member of an organization/institution",
        choices=MEMBER_ORGANIZATION_INSTITUTION,
        blank=False, 
        max_length=5,
    )
    org_inst = models.CharField(
        verbose_name="Organization/Institution name",
        max_length=100,
    )
    tel = models.CharField(
        verbose_name="Tel",
        max_length=100,
    )
