from rest_framework import viewsets
from rest_framework import permissions

from projects.models import Project, Technology, DevelopmentMethodology, ProjectField
from api.serializers import ProjectSerializer, TechnologySerializer, DevelopmentMethodologySerializer, ProjectFieldSerializer



class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]



class TechnologyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.IsAuthenticated]



class DevelopmentMethodologyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DevelopmentMethodology.objects.all()
    serializer_class = DevelopmentMethodologySerializer
    permission_classes = [permissions.IsAuthenticated]



class ProjectFieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ProjectField.objects.all()
    serializer_class = ProjectFieldSerializer
    permission_classes = [permissions.IsAuthenticated]
