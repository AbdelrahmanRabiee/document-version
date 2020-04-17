from rest_framework import serializers
from documents.models import VersionControlPloicy, UserDocument

class UserDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDocument
        fields = ['id', 'doc_type', 'document']