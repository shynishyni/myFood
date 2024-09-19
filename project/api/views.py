from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import FoodSerializer  
from django.http.response import JsonResponse

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
