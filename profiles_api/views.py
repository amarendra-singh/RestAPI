from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import permissions

from profiles_api import models

# Create your views here.
class Detail(APIView):
    serializer_class = serializers.DetailsSerializer

    def get(self, request, format = None):
        return Response ({'message':'Hello'})

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            print(name)
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        return Response({'method':'patch'})
    
    def delete(self, request, pk=None):
        return Response({'method':'delete'})

class DetailViewSet(viewsets.ViewSet):
    serializer_class = serializers.DetailsSerializer
    
    def list(self, request):
        return Response({'meesage':'hello'})

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_REQUEST)

    def retrieve (Self, request, pk = None):
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response ({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

