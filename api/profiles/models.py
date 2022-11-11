from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from api.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class PaymentStatus(models.TextChoices):
    NONE = "None", _("None")
    TRIER = "Trier", _("Trier")
    PAID = "Paid", _("Paid")
    FINISHED = "Finished", _("Finished")


class Package(models.TextChoices):
    STARTER = "Starter", _("Starter")
    PREMIUM = "Premium", _("Premium")
    ENTERPRISE = "Enterprise", _("Enterprise")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"),
        default="US",
        blank=True,
        null=True,
    )
    state = models.CharField(
        verbose_name=_("State"),
        max_length=180,
        default="LA",
        blank=True,
        null=True,
    )
    payment_status = models.CharField(
        verbose_name=_("Payment Status"),
        choices=PaymentStatus.choices,
        default=PaymentStatus.NONE,
        max_length=20,
    )
    package = models.CharField(
        verbose_name=_("Gender"),
        choices=Package.choices,
        default=Package.STARTER,
        max_length=20,
    )
    expired_at = models.DateTimeField(
        verbose_name=_("Expired At"),
        blank=True,
        null=True,
    )
    num_of_months = models.IntegerField(
        verbose_name=_("Number of Months"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
