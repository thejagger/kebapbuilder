from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
from kebapbuilder.models import Order, Type, MainType, Additional, Person

class IndexView(generic.ListView):
    template_name = 'kebapbuilder/order_list.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        return Order.objects.order_by('-person')
    
class AddView(generic.CreateView):
    model = Order
    fields = ['person', 'type', 'main_type', 'additionals']
    template_name = 'kebapbuilder/order_detail.html'