from django.db import models
from django.utils.translation import gettext_lazy as _

class OrganizationUnit(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    manager_email = models.EmailField(max_length=255, verbose_name=_("Manager Email"), blank=True, null=True)
    manager_name = models.CharField(max_length=255, verbose_name=_("Manager Name"), blank=True, null=True)
    manager_title = models.CharField(max_length=255, verbose_name=_("Manager Title"), blank=True, null=True)
    manager_level = models.CharField(max_length=20, verbose_name=_("Manager Level"), blank=True, null=True)
    manager_level_desc = models.CharField(max_length=255, verbose_name=_("Manager Level Description"), blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True, verbose_name=_("Parent Unit"))

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'ORGANIZATION_UNITS'
        verbose_name = _("Organization Unit")
        verbose_name_plural = _("Organization Units")
