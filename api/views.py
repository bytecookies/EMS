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

from rest_framework import filters
from .pagination import *
from core.models import Exhibitor, Visitor, Meeting
from utility.models import Brand, Nationality, NatureOfBusiness, Department, ProductCatogory, ProductSubCatogory
from .serializers import *
from .permissions import *
from django.db.models import Q


# Create your views here.

@api_view()
def index(request):
   
    return Response("ok")

class ExhibitorWithKey(ReadOnlyModelViewSet):
    
    queryset=Exhibitor.objects.select_related('user').prefetch_related('our_brand','nature_of_bussiness','product_catogory','product_sub_catogory').filter(Q(user__participation_form=True)).order_by('companyName').distinct()
    serializer_class= ExhibitorDetailSerializer
    # filter_backends=[filters.SearchFilter]
    # search_fields=['companyName','our_brand__name','nature_of_bussiness__name','product_catogory__name']
    # permission_classes = [HasAPIKey]
    


class ExhibitorViewSet(ReadOnlyModelViewSet):
    queryset=Exhibitor.objects.select_related('user').prefetch_related('our_brand','nature_of_bussiness','product_catogory','product_sub_catogory').filter(Q(user__participation_form=True)).order_by('companyName').distinct()
    serializer_class= ExhibitorDetailSerializer
    permission_classes = [IsAuthenticated,IsVisitorUser]
    pagination_class= StandardResultsSetPagination
    filter_backends=[filters.SearchFilter]
    search_fields=['companyName','our_brand__name','nature_of_bussiness__name','product_catogory__name']
    
    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return ExhibitorDetailSerializer
      
    #     return ExhibitorListSerializer
    

class CreatMeetingViewSet(ModelViewSet):
    
    queryset=Meeting.objects.all()
    serializer_class=MeetingSerializer
    permission_classes = [IsAuthenticated,IsVisitorUser]
    
    def get_queryset(self):
    
        queryset=Meeting.objects.select_related('sender').filter(sender=self.request.user)
        return queryset
    
    # def create(self, request, *args, **kwargs):
    #     user = request.user
    #     # data = {
    #     #     "title": request.POST.get('title', None),
    #     #     }
    #     print(request.data)
    #     serializer = self.serializer_class(data=request.data,
    #                                        context={'author': user})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
   

class VisitorViewSet(ReadOnlyModelViewSet):
    queryset=Visitor.objects.all()
    serializer_class=VisitorListSerializer
    permission_classes = [IsAuthenticated,IsExhibitorUser]


class VisitorProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,GenericViewSet):
    queryset=Visitor.objects.select_related('user').select_related('nationality').select_related('department').prefetch_related('nature_of_business').prefetch_related('product_category').prefetch_related('product_sub_category').prefetch_related('brand').prefetch_related('product_category_interest').prefetch_related('product_sub_category_interest').prefetch_related('how_did_you_get_to_know_about_INTIMASIA').all()
    serializer_class=VisitorDetailSerializer
    permission_classes = [IsAuthenticated,IsVisitorUser]
    
    
    

    @action(detail=False, methods=['GET','PUT'])
    def me(self, request):
        
        visitor=Visitor.objects.select_related('user').select_related('nationality').select_related('department').prefetch_related('nature_of_business').prefetch_related('product_category').prefetch_related('product_sub_category').prefetch_related('brand').prefetch_related('product_category_interest').prefetch_related('product_sub_category_interest').prefetch_related('how_did_you_get_to_know_about_INTIMASIA').get(user_id=request.user.id)
        
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
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['name']
    ordering_fields = ['name']

class DepartmentViewSet(ReadOnlyModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['name']
    ordering_fields = ['name']


class NatureOfBusinessViewSet(ReadOnlyModelViewSet):
    queryset=NatureOfBusiness.objects.all()
    serializer_class=NatureOfBusinessSerializer
    permission_classes = [IsAuthenticated]
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['name']
    ordering_fields = ['name']

class ProductCatogoryViewSet(ReadOnlyModelViewSet):
    queryset=ProductCatogory.objects.all()
    serializer_class=ProductCatogorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['name']
    ordering_fields = ['name']

class ProductSubCatogoryViewSet(ReadOnlyModelViewSet):
    queryset=ProductSubCatogory.objects.all()
    serializer_class=ProductSubCatogorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['name']
    ordering_fields = ['name']



class NationalityViewSet(ReadOnlyModelViewSet):
    queryset=Nationality.objects.all()
    serializer_class=NationalitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['name']
    ordering_fields = ['name']



