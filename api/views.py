from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.decorators import action
from core.models import Exhibitor, Visitor
from utility.models import Brand, Nationality, NatureOfBusiness, Department, ProductCatogory, ProductSubCatogory
from .serializers import *
from .permissions import *
from django.db.models import Q

# Create your views here.

@api_view()
def index(request):
   
    return Response("ok")



class ExhibitorViewSet(ReadOnlyModelViewSet):
    queryset=Exhibitor.objects.select_related('user').filter(Q(user__participation_form=True)).order_by('companyName').distinct()
    # serializer_class= ExhibitorSerializer
    permission_classes = [IsAuthenticated,IsVisitorUser]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ExhibitorDetailSerializer
      
        return ExhibitorListSerializer
    
    

    
   

class VisitorViewSet(ReadOnlyModelViewSet):
    queryset=Visitor.objects.all()
    serializer_class=VisitorListSerializer
    permission_classes = [IsAuthenticated,IsExhibitorUser]


class VisitorProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,GenericViewSet):
    queryset=Visitor.objects.all()
    serializer_class=VisitorDetailSerializer
    permission_classes = [IsAuthenticated,IsVisitorUser]
    

    @action(detail=False, methods=['GET','PUT'])
    def me(self, request):
        visitor=Visitor.objects.get(user_id=request.user.id)
        if request.method=='GET':
            serializer=VisitorDetailSerializer(visitor)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=VisitorDetailSerializer(visitor,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)





class VisitorCreate(mixins.CreateModelMixin,GenericViewSet):
    queryset=Visitor.objects.all()
    serializer_class=VisitorCreateSerializer
    



    



# class ExhibitorDetails(ListAPIView):
#     # def get_queryset(self,id):
#     #     return get_object_or_404(Exhibitor, pk=id)
#     # def get_serializer_class(self):
#     #     return ExhibitorSerializer

#     def get(self,request,pk):
#         exhibitor=get_object_or_404(Exhibitor, pk=pk)
#         serilizer=ExhibitorSerializer(exhibitor)
#         return Response(serilizer.data)


# class VisitorList(APIView):
#     def get(self,request):
#         queryset=Visitor.objects.all()
#         serilizer=VisitorSerializer(queryset,many=True)
#         return Response(serilizer.data)



# @api_view()
# def exhibitor_list  (request):
#     queryset=Exhibitor.objects.all()
#     serilizer=ExhibitorSerializer(queryset,many=True)
#     return Response(serilizer.data)

# @api_view()
# def exhibitor_detail(request,id):
#     exhibitor=get_object_or_404(Exhibitor, pk=id)
 
#     serilizer=ExhibitorSerializer(exhibitor)
#     return Response(serilizer.data)

 


# utility ViewSet

class BrandViewSet(ReadOnlyModelViewSet):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    permission_classes = [IsAuthenticated]

class DepartmentViewSet(ReadOnlyModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes = [IsAuthenticated]


class NatureOfBusinessViewSet(ReadOnlyModelViewSet):
    queryset=NatureOfBusiness.objects.all()
    serializer_class=NatureOfBusinessSerializer
    permission_classes = [IsAuthenticated]

class ProductCatogoryViewSet(ReadOnlyModelViewSet):
    queryset=ProductCatogory.objects.all()
    serializer_class=ProductCatogorySerializer
    permission_classes = [IsAuthenticated]

class ProductSubCatogoryViewSet(ReadOnlyModelViewSet):
    queryset=ProductSubCatogory.objects.all()
    serializer_class=ProductSubCatogorySerializer
    permission_classes = [IsAuthenticated]



class NationalityViewSet(ReadOnlyModelViewSet):
    queryset=Nationality.objects.all()
    serializer_class=NationalitySerializer
    permission_classes = [IsAuthenticated]



