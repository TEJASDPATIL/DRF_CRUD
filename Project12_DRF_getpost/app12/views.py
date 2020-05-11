import io

from django.http import HttpResponse
from django.shortcuts import render
from django.db.utils import IntegrityError
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError

from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView
from app12.models import ProductModel
from .serializers import ProductSerializers
# class ProductOperations(View):
#     def post(self,request):
#         try:
#             d1 = JSONParser().parse(io.BytesIO(request.body))
#             ps = ProductSerializers(data=d1)
#             try:
#                 if ps.is_valid():
#                     ps.save()
#                     message = {"Success":"Product Saved"}
#                 else:
#                     message = {"Error":ps.errors}
#                 return HttpResponse(JSONRenderer().render(message),content_type="app/json")
#             except IntegrityError:
#                 message = {"Error":"Product of given id already available"}
#                 return HttpResponse(JSONRenderer().render(message), content_type="app/json")
#         except ParseError:
#             message = {"Error": "Please Provide Product Details to Save.Cant Proceed with empty details."}
#             return HttpResponse(JSONRenderer().render(message), content_type="app/json")
#
#     def get(self,request):
#         try:
#             d1 = JSONParser().parse(io.BytesIO(request.body))
#             if d1:
#                 pno = d1['no']
#                 try:
#                     one = ProductModel.objects.get(no=pno)
#                     ps = ProductSerializers(one)
#
#                     return HttpResponse(JSONRenderer().render(ps.data),content_type="app/json")
#                 except ProductModel.DoesNotExist:
#                     message = {"Error": "Product of Entered Product Number is not available in DB"}
#                     return HttpResponse(JSONRenderer().render(message), content_type="app/json")
#
#
#             else:
#                 all = ProductModel.objects.all()
#                 ps = ProductSerializers(all,many=True)
#                 return HttpResponse(JSONRenderer().render(ps.data),content_type="app/json")
#         except ParseError:
#             message = {"Error": "Please Provide Product Number or empty dict to retrieve details."}
#             return HttpResponse(JSONRenderer().render(message), content_type="app/json")
#
#     def put(self,request):
#         try:
#             d1 = JSONParser().parse(io.BytesIO(request.body))
#             pno = d1.get("no")
#             if pno:
#                 try:
#                     pr = ProductModel.objects.get(no=pno)
#                     ps = ProductSerializers(pr,d1,partial=True)
#                     if ps.is_valid():
#                         ps.save()
#                         message = {"Success":"Product is Updated"}
#                     else:
#                         message = {"Error":ps.errors}
#                 except ProductModel.DoesNotExist:
#                     message = {"Error": "Product of give product number not available in DB"}
#             else:
#                 message = {"Error": "Please provide valid Data"}
#
#         except ParseError:
#             message = {"Error":"Please Provide  Product Number and Details"}
#         return HttpResponse(JSONRenderer().render(message),content_type="app/json")
#
#     def delete(self,request):
#         try:
#             d1 = JSONParser().parse(io.BytesIO(request.body))
#             pno = d1.get("no")
#             if pno:
#                 pm =ProductModel.objects.filter(no=pno).delete()
#                 if pm[0] != 0:
#                     message = {"Success":"Product Deleted Successfully"}
#                 else:
#                     message = {"Success":"Product of given number not available..."}
#             else:
#                 message = {"Success": "Please provide product number..."}
#
#
#         except ParseError:
#             message = {"Error":"Please Provide  Product Number to DELETE!!!"}
#         return HttpResponse(JSONRenderer().render(message),content_type="app/json")
class ProductListView(ListAPIView):
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()

class ProductCreateApiView(CreateAPIView):
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()

class ProductDetailApiView(RetrieveAPIView):
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()

class ProductDeleteApiView(DestroyAPIView):
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()



