from django.urls import path

from rest_framework import routers

from documents.viewsets import UserDocumentViewSet

app_name = "documents"
urlpatterns = [

]

documents_router = routers.SimpleRouter()

documents_router.register(r'document', UserDocumentViewSet, base_name='document')