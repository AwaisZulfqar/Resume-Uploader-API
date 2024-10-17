from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework import viewsets
from rest_framework import status
from .models import Profile

# Create your views here.



class ProfileView(viewsets.ViewSet):

    def create(self,request):
        prf = ProfileSerializer(data=request.data)
        if prf.is_valid():
            prf.save()
            return Response({'msg':'Profile succesfully Added','profile':prf.data},status=status.HTTP_201_CREATED)
        return Response(prf.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(seld,request):
        prf = Profile.objects.all()
        serailizer = ProfileSerializer(prf,many=True)
        return Response(serailizer.data)
    