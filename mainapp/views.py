from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serilaizers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
import jwt as JWT_
from diplom.settings import SIMPLE_JWT
# Create your views here.
#########################################



# Refresh TokenObtainPairView (add user)
class AuthorizateView(TokenObtainPairView):
    serializer_class = AuthorizateSerializer


class IsAuthView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        refresh_token_get = request.META.get('HTTP_AUTHORIZATION', ' ').split(' ')[1]
        jwt=JWT_.decode(
            refresh_token_get,
            SIMPLE_JWT['SIGNING_KEY'],
        algorithms = [SIMPLE_JWT['ALGORITHM']],
            )
        
        queryset=User.objects.get(id=jwt['user_id'])
        serilaizers= UserSerilizer(queryset)
        return Response({'user':serilaizers.data}, status=status.HTTP_200_OK)
    

class LogoView(generics.GenericAPIView):
    serializer_class = LogoSerilezer
    
    def get(self, request, *args, **kwargs):
        queryset=Logo.objects.filter().first()
        serilaizers= LogoSerilezer(queryset)
        return Response(serilaizers.data, status=status.HTTP_200_OK)


class PatkingView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ParkingSerilezer
    def post(self, request):

        electron = Parking.objects.filter(id_Parking = request.data['id_Parking'])
        if electron.exists():
            data = electron.first()
            data.number = request.data['number']
            
            data.save()
            return Response(ParkingSerilezer(data).data,status=status.HTTP_200_OK)
        else:
            data = Parking.objects.create(id_Parking = request.data['id_Parking'],number = request.data['number'],  )
            
            return Response(ParkingSerilezer(data).data,status=status.HTTP_200_OK)


class ParkingGet(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ParkingSerilezer
    def get(self, request):
        queryset=Parking.objects.filter().first()
        serilaizers= ParkingSerilezer(queryset)
        return Response(serilaizers.data, status=status.HTTP_200_OK)
    

class StolView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    def post(self, request):

        electron = Stol.objects.filter(id_stol = request.data['id_stol'])
        if electron.exists():
            data = electron.first()
            data.parsing_data = request.data['parsing_data']
            if int(request.data['parsing_data']) == 1:
                data.stol1 = True
            if int(request.data['parsing_data']) == 2:
                data.stol2 = True
            if int(request.data['parsing_data']) == 3:
                data.stol3 = True
            if int(request.data['parsing_data']) == 4:
                data.stol4 = True
            if int(request.data['parsing_data']) == 5:
                data.stol5 = True
            if int(request.data['parsing_data']) == 6:
                data.stol6 = True
            if int(request.data['parsing_data']) == 7:
                data.stol7 = True
            if int(request.data['parsing_data']) == 8:
                data.stol8 = True
            
            data.save()
            return Response(StolSerilezer(data).data,status=status.HTTP_200_OK)
        else:
            data = 0
            if int(request.data['parsing_data']) == 1:
                data = Stol.objects.create(id_stol = int(request.data['id_stol']),
                                        parsing_data = int(request.data['parsing_data']),
                                        stol1 = True,
                                            )
            if int(request.data['parsing_data']) == 2:
                data = Stol.objects.create(id_stol = int(request.data['id_stol']),
                                        parsing_data = int(request.data['parsing_data']),
                                        stol2 = True,
                                            )
            if int(request.data['parsing_data']) == 3:
                data = Stol.objects.create(id_stol = int(request.data['id_stol']),
                                        parsing_data = int(request.data['parsing_data']),
                                        stol3 = True,
                                            )
            if int(request.data['parsing_data']) == 4:
                data = Stol.objects.create(id_stol = int(request.data['id_stol']),
                                        parsing_data = int(request.data['parsing_data']),
                                        stol4 = True,
                                            )
            if int(request.data['parsing_data']) == 5:
                data = Stol.objects.create(id_stol = int(request.data['id_stol']),
                                        parsing_data = int(request.data['parsing_data']),
                                        stol5 = True,
                                            )
            if int(request.data['parsing_data']) == 6:
                data = Stol.objects.create(id_stol = int(request.data['id_stol']),
                                        parsing_data = int(request.data['parsing_data']),
                                        stol6 = True,
                                            )
            if int(request.data['parsing_data']) == 7:
                data = Stol.objects.create(id_stol = int(request.data['id_stol']),
                                        parsing_data = int(request.data['parsing_data']),
                                        stol7 = True,
                                            )
            if int(request.data['parsing_data']) == 8:
                data = Stol.objects.create(id_stol = int(request.data['id_stol']),
                                        parsing_data = int(request.data['parsing_data']),
                                        stol8 = True,
                                            )
            
            return Response(StolSerilezer(data).data,status=status.HTTP_200_OK)