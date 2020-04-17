from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from documents.serializers import UserDocumentSerializer
from documents.models import UserDocument, VersionControlPloicy


class UserDocumentViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    
    """
    serializer_class = UserDocumentSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserDocument.objects.none()

    def list(self, request, *args, **kwargs):
        """Get logged-in user's documents based on version."""

        version = request.GET.get('v')
        if version is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = self.request.user
        version = VersionControlPloicy.objects.filter(ver_title=version)
        if version.exists():
            version = version.first()
            query_fields = version.policy.split(',')    
            documents = user.documents.filter(doc_type__in=query_fields)
            serializer = self.get_serializer(documents, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)    