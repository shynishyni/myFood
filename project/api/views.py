from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import FoodSerializer  
from django.http.response import JsonResponse
from .models import FoodDetails

@csrf_exempt
def recipes(request):
    if request.method == 'POST':
        data = request.POST.dict()
        if request.FILES:
            data['pic1'] = request.FILES.get('pic1')
            data['pic2'] = request.FILES.get('pic2')
        serializer = FoodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"recipy": "Recipe added successfully"}, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
    if request.method == 'GET':
        item= FoodDetails.objects.all()
        serializer = FoodSerializer(item,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def getrecipe(request,id=0):
    if request.method == "GET":
        if id == 0:
            return JsonResponse({"message": "Item not found :("}, status=404)
        else:
            try:
                data = FoodDetails.objects.get(id=id)
                serializer = FoodSerializer(data)
                return JsonResponse(serializer.data, safe=False)
            except FoodDetails.DoesNotExist:
                return JsonResponse({"message": "Item not found :("}, status=404)
            except Exception as e:
                return JsonResponse({"message": str(e)}, status=500)
@csrf_exempt
def getbyarea(request,area=''):
     if request.method == 'GET':
          if (area=='All' or area==""):
               recipes=FoodDetails.objects.all()
               serializer = FoodSerializer(recipes,many=True)
               return JsonResponse(serializer.data,safe=False)
          else:
               try:
                    recipes = FoodDetails.objects.filter(area__icontains=area)
                    if recipes.exists():
                         serializer=FoodSerializer(recipes,many=True)
                         return JsonResponse(serializer.data,safe=False)
                    else:
                         return JsonResponse({"message":"Item not found"}, status=404)
               except FoodDetails.DoesNotExist:
                    return JsonResponse({"message":"Item not found"},status=404)
