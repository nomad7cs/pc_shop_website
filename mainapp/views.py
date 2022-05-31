from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import Computer
from .forms import PcItemForm


# Read Operation
def index(request):
    latest_computer_list = Computer.objects.order_by('-registration_date')[:15]
    template = loader.get_template('mainapp/index.html')
    context = {
        'latest_computer_list': latest_computer_list,
    }
    return HttpResponse(template.render(context, request))

# Parametric request
def pc_details(request, computer_id):
    try:
        pc = Computer.objects.get(pk=computer_id)
        template = loader.get_template('mainapp/pc_details.html')
        context = {'pc': pc,}
    except Computer.DoesNotExist:
        raise Http404("Computer does not exist")
    return HttpResponse(template.render(context, request))

def pc_item_details(request, pc_item_id):
    try:
        pc_item = ComputerPart.objects.get(pk=pc_item_id)
        template = loader.get_template('mainapp/pc_item_details.html')
        context = {'pc_item': pc_item,}
    except ComputerPart.DoesNotExist:
        raise Http404("PC Item does not exist")
    return HttpResponse(template.render(context, request))

# Create/Update Operation.  PUT|GET request
def pc_item_form_view(request, instance_id):
    if request.method == 'POST':
        form = None
        if instance_id:
            instance_obj = ComputerPart.objects.get(pk=instance_id)
            form = PcItemForm(request.POST, instance= instance_obj)
        else:
            form = PcItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PcItemForm()
        return render(request, 'pc_item_form.html', {'form': form})
