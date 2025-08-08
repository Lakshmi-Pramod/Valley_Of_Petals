from rest_framework import serializers
from .models import flora
from .models import habitat
from .models import characteristics
from .models import can_view
from .models import viewer_email
from .models import Viewer
from .models import marketValue
from .models import Notification
class floraSerializer(serializers.ModelSerializer):
    class Meta:
        model=flora
        fields=('id','flora_id','species','region','evaluated_date')

class habitatSerializer(serializers.ModelSerializer):
    class Meta:
        model=habitat
        fields=('id','climate','altitude_range','season','soil','flora_id')

class characteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model=characteristics
        fields=('id','b_name','utility','avail','flora_id')

class can_viewSerializer(serializers.ModelSerializer):
    class Meta:
        model=can_view
        fields=('id','flora_id','v_id')

class viewer_emailSerializer(serializers.ModelSerializer):
    class Meta:
        model=viewer_email
        fields=('id','email','v_id')

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Viewer
        fields=('id','v_id','uname','psd','city','state','pin')

class marketvalueSerializer(serializers.ModelSerializer):
    class Meta:
        model=marketValue
        fields=('id','item_id','flora_id','cons','exp','cost')
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=('id','n_id','flora_s','login_date','t_in','t_out','v_id')
