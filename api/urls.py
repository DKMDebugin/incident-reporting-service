from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
                    FrequencyViewset, TypeViewset,
                    DefinitionViewset, ReportViewset,
                    )

# bind url to viewsets
frequency_list = FrequencyViewset.as_view({
            "get": "list",
        })
type_list = TypeViewset.as_view({
            "get": "list",
        })
definition_detail = DefinitionViewset.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        })
definition_list = DefinitionViewset.as_view({
            "get": "list",
            "post": "create",
            "delete": "bulk_delete"
        })

# wire up the views with urls
router = DefaultRouter()
router.register(r"frequencies", FrequencyViewset)
router.register(r"types", TypeViewset)
router.register(r"definitions", DefinitionViewset)

urlpatterns = [
    path("", include(router.urls)),
]
