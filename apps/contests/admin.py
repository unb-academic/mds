from typing import TYPE_CHECKING

from django.contrib.admin import ModelAdmin, register
from django.forms import (
    CharField,
    ModelForm,
    ModelMultipleChoiceField,
    Textarea,
)
from django.utils.translation import gettext_lazy as _

from apps.contests.models import Contest
from apps.users.models import User

if TYPE_CHECKING:
    ContestAdminBase = ModelAdmin[Contest]
    ContestModelFormBase = ModelForm[Contest]
else:
    ContestAdminBase = ModelAdmin
    ContestModelFormBase = ModelForm


class ContestModelForm(ContestModelFormBase):
    description = CharField(widget=Textarea(attrs={"rows": 14, "cols": 80}))
    users = ModelMultipleChoiceField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Contest
        fields = "__all__"


@register(Contest)
class ContestAdmin(ContestAdminBase):
    form = ContestModelForm

    list_display = ("title", "start_time", "end_time", "status")
    list_filter = ("start_time", "end_time")

    fieldsets = [
        (_("General"), {"fields": ("title", "description")}),
        (
            _("Other"),
            {"fields": ("start_time", "end_time", "users", "cancelled")},
        ),
    ]
