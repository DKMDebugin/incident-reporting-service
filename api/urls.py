from django.urls import path, include
from rest_framework.routers import DefaultRouter, Route

from .views import (
                    FrequencyViewset, TypeViewset,
                    DefinitionViewset, ReportViewset,
                    # DefinitionBulkDelete, definition_bulk_delete
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
            "delete": "bulk_destroy",
        })
definition_list = DefinitionViewset.as_view({
            "get": "list",
            "post": "create",
        })


# class BulkDeleteRouter(DefaultRouter):
#     """
#     a custom URL router for the  that correctly routes
#     DELETE requests with multiple query parameters.
#     """
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.routes += [
#             Route(
#                 url=r'^{prefix}{trailing_slash}$',
#                 mapping={'delete': 'bulk_destroy'},
#                 name='{basename}-delete',
#                 initkwargs={'suffix': 'Delete'},
#                 detail=""
#             ),
#         ]

# wire up the views with urls
router = DefaultRouter()
# bulk_delete_router = BulkDeleteRouter()
router.register(r"frequencies", FrequencyViewset)
router.register(r"types", TypeViewset)
router.register(r"definitions", DefinitionViewset)
# bulk_delete_router.register(r"definitions/bulk_delete", DefinitionViewset, basename="bulk")

urlpatterns = [
    # path("definitions/bulk_delete/", definition_bulk_delete, name="bulk_delete"),
    # path("definitions/bulk_delete/", DefinitionBulkDelete.as_view(), name="bulk_delete"),
    # url('^purchases/(?P<username>.+)/$', PurchaseList.as_view()),
    path("", include(router.urls)),
    # path("", include(bulk_delete_router.urls)),
]
