from django.shortcuts import render
from .models import ViewingActivity
from django.db.models import Count
# Create your views here.
def home(request):
    profile_name = "Chiamaka"  #Using only my data
    most_streamed = (ViewingActivity.objects
                     .filter(profile_name=profile_name)
                     .values("title")
                     .annotate(title_count=Count("title"))
                     .order_by('-title_count')
                     .first()
                     )
    most_streamed_show = (ViewingActivity.objects
                     .filter(profile_name=profile_name, title_icontains="episode")
                     .values("title")
                     
                     )
                     