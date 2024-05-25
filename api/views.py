from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import Registration,User,Todoserializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from work.models import Taskmodel
from rest_framework import serializers

# Create your views here.

class Userregister(APIView):

    def post(self,request,*args,**kwargs):

        serializer=Registration(data=request.data)

        if serializer.is_valid():

            serializer.save()

        return Response  (serializer.data)
    
class Todoviewsetview(ViewSet):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):

        qs=Taskmodel.objects.all()

        serializer=Todoserializer(qs,many=True)

        return Response(serializer.data)
    
    def create(self,request,*args,**kwargs):

        serializer=Todoserializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

        return Response(serializer.data)
    
    def destroy(self,request,*args,**kwargs):

        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)

        if qs.user==request.user:
            qs.delete()
            return Response({'message':'object deleted'})
        else:
            raise serializers.ValidationError('qwerty')
        
    def update(self,request,*args,**kwargs):

        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)

        serializer=Todoserializer(data=request.data,instance=qs)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        serializer=Todoserializer(qs)

        return Response(serializer.data)
    
class Todomodelview(ModelViewSet):
    queryset=Taskmodel.objects.all()
    serializer_class=Todoserializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)




