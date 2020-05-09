from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    FrequencyViewset, TypeViewset,
    DefinitionViewset, ReportViewset )

# bind url to viewsets
frequency_list = FrequencyViewset.as_view({
    "get": "list",
})
type_list = TypeViewset.as_view({
    "get": "list",
})

# wire up the views with urls
router = DefaultRouter()
router.register(r"frequencies", FrequencyViewset, )
router.register(r"types", TypeViewset)
router.register(r"definitions", DefinitionViewset)
router.register(r"reports", ReportViewset)

urlpatterns = [

    path("", include(router.urls)),

]
