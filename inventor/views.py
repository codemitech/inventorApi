from rest_framework.response import Response
from .serializers import InvestorCustomRegistrationSerializer, InventorCustomRegistrationSerializer, InvestorUpdateSerializer, UserSerializer, InvestorUpdateSerializer, InventorUpdateSerializer,InventionSerializer,InvestmentSerializer,Trimmedinventions
from rest_framework import generics,status,permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsInventor, IsInvestor
from .models import *

#inventor-sign-up
class Inventorsignup(generics.GenericAPIView):
    serializer_class = InventorCustomRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
            
        })


#investor-sign-up
class Investorsignup(generics.GenericAPIView):
    serializer_class = InvestorCustomRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
            
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']

        token, created= Token.objects.get_or_create(user=user)

        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_inventor':user.is_inventor
        })

#Logout
class LogOutView(APIView):
    def post(self, request, *args, **kwargs):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

#investor-only
class InvestorOnly(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsInvestor]

    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

#inventor-only
class InventorOnly(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsInventor]
    serializer_class=UserSerializer
    def get_object(self):
        return self.request.user

#investor-update
class InvestorUpdateView(generics.UpdateAPIView):
     queryset = User.objects.all()
     permission_classes =[permissions.IsAuthenticated&IsInvestor]
     serializer_class = InvestorUpdateSerializer

     """def get_qureyset(self):
       user = self.request.user
       return user.investor.all()
 """
#inventor-update
class InventorUpdateView(generics.UpdateAPIView):
     queryset = User.objects.all()
     permission_classes =[permissions.IsAuthenticated&IsInventor]
     serializer_class = InventorUpdateSerializer

     """def get_queryset(self):
       user = self.request.user
       """


#inventions
class AllInventionsView(generics.ListCreateAPIView):
    queryset = inventions.objects.all()
    serializer_class = InventionSerializer

#investment-endpoint
class AllInvestmentView(generics.ListCreateAPIView):
    queryset = investment.objects.all()
    serializer_class = InvestmentSerializer

#trimmed inventions view
class InventionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = inventions.objects.all()
    serializer_class = InventionSerializer 


    


        


   
