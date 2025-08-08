from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from rest_framework import viewsets
from .serializers import floraSerializer
from .serializers import habitatSerializer
from .serializers import characteristicsSerializer
from .serializers import can_viewSerializer
from .serializers import viewer_emailSerializer
from .serializers import ViewerSerializer
from .serializers import marketvalueSerializer
from .serializers import NotificationSerializer

from .models import flora
from .models import habitat
from .models import characteristics
from .models import can_view
from .models import viewer_email
from .models import Viewer
from .models import marketValue
from .models import Notification
# Create your views here.
def get_flora_records(request):
    records=flora.objects.all().values()
    return JsonResponse(list(records),safe=False)
'''
def get_filter_options(request, attribute):
    options=[]
    if attribute == 'utility':
        options = characteristics.objects.values_list('utility', flat=True).distinct()
    elif attribute == 'season':
        options = habitat.objects.values_list('season', flat=True).distinct()
    elif attribute == 'soil':
        options = habitat.objects.values_list('soil', flat=True).distinct()
    
    elif attribute == 'region':
        options = flora.objects.values_list('region', flat=True).distinct()
    elif attribute == 'consumer':
        options = marketValue.objects.values_list('cons', flat=True).distinct()
    return JsonResponse(list(options), safe=False)



def get_flora_details(request, title):
    try:
        flora = flora.objects.get(title=title)
        # Assuming flora_id is the field in the Flora model corresponding to f_id
        flora_details = {
            'Flora_id': flora.flora_id,
            'Species': flora.species,
            'Region':flora.region,
            'Evaluated_date':flora.evaluated_date,
            # Add other fields you want to retrieve
        }
        return JsonResponse(flora_details)
    except flora.DoesNotExist:
        return JsonResponse({'error': 'Flora not found'}, status=404)
   
    return JsonResponse(data, safe=False)
    '''
class floraView(viewsets.ModelViewSet):
    serializer_class=floraSerializer
    queryset=flora.objects.all()

class habitatView(viewsets.ModelViewSet):
    serializer_class=habitatSerializer
    queryset=habitat.objects.all()

class characteristicsView(viewsets.ModelViewSet):
    serializer_class=characteristicsSerializer
    queryset=characteristics.objects.all()

class can_viewView(viewsets.ModelViewSet):
    serializer_class=can_viewSerializer
    queryset=can_view.objects.all()

class viewer_emailView(viewsets.ModelViewSet):
    serializer_class=viewer_emailSerializer
    queryset=viewer_email.objects.all()

class ViewerView(viewsets.ModelViewSet):
    serializer_class=ViewerSerializer
    queryset=Viewer.objects.all()

class marketValueView(viewsets.ModelViewSet):
    serializer_class=marketvalueSerializer
    queryset=marketValue.objects.all()

class NotificationView(viewsets.ModelViewSet):
    serializer_class=NotificationSerializer
    queryset=Notification.objects.all()