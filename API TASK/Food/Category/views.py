from django.shortcuts import render
from . models import CategoryModel
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status 



# Create your views here.
class CategoryViewset(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
 
    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        elif self.action == 'create':
            return CategorySerializer
        return self.serializer_class
 
#get all authors
    def list(self,request):
        try:
            category_objs = CategoryModel.objects.all()
            serializer = self.get_serializer(category_objs,many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'data':serializer.data
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
#add an CategoryModel
    def create(self,request):
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'CategoryModel Added Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
#get single CategoryModel
 
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:
                category_objs = self.get_object()
                serializer = self.get_serializer(category_objs)
                return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
#update all fields of CategoryModel
    def update(self,request):
        try:
            category_objs = self.get_object()
            serializer = self.get_serializer(category_objs,data=request.data,partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'CategoryModel Updated Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
 
 
#update specifie
    def partial_update(self,request):
        try:
            category_objs = self.get_object()
            serializer = self.get_serializer(category_objs,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'CategoryModel Partial Updated Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
    def destroy(self,request,pk):
        try:
            id=pk
            category_objs = self.get_object()
            category_objs.delete()
 
            return Response({
                'status': status.HTTP_200_OK,
                'message':'CategoryModel deleted successfully'
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })