from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from services.models import Services, ServiceProvider, ProviderMessage, AdminMessage
from services.forms import ProviderMessageForm, AdminMessageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def view_service(request, service_provider, service_name):
    service = Services.objects.get(title=service_name, service_provider__sp_name=service_provider, status='active')
    service_provider = ServiceProvider.objects.filter(sp_name=service_provider).first()
    
    return render(request, 'view_service.html', {
        'service': service,
        'service_provider': service_provider,
    })

def contactProvider(request, service_provider, service_name):
    service = Services.objects.get(title=service_name, service_provider__sp_name=service_provider, status='active')
    service_provider = ServiceProvider.objects.filter(sp_name=service_provider).first()
    if request.method == 'POST':
        form = ProviderMessageForm(request.POST)
        if form.is_valid():
            # modify subject field by pass the service instance to the form using the instance parameter
            form.instance.subject = "Query about service %s" % service.title
            form.save()
            messages.success(request, "Success")
            form = ProviderMessageForm()
        else:
            messages.error(request, "Failed")
    else:
        form = ProviderMessageForm()
    return render(request, 'contactProvider.html', {'form': form})


@login_required
def contactAdmin(request):
    user = request.user
    if request.method == 'POST':
        form = AdminMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.name = user.get_full_name()
            message.email = user.email
            message.save()
            messages.success(request, "Success")
            form = AdminMessageForm()
        else:
            messages.error(request, "Failed")
    else:
        form = AdminMessageForm(initial={'name': user.get_full_name(), 'email': user.email})
        form.fields['name'].widget.attrs['readonly'] = True
        form.fields['email'].widget.attrs['readonly'] = True
    return render(request, 'contactAdmin.html', {'form': form})


def services(request):
    popular_service_providers = ServiceProvider.objects.order_by('sp_star')[0:4]
    popular_services = Services.objects.filter(status=Services.ACTIVE).order_by('stars')[0:4]
    all_services = Services.objects.all()
    return render(request, 'services.html', {
    'popular_service_providers': popular_service_providers,
    'popular_services': popular_services,
    'all_services': all_services
    })


def search_services(request):
    service_query = request.GET.get('service_query', '')
    services = None
    service_provider = None
    if service_query:
        services = Services.objects.filter(status=Services.ACTIVE).filter(Q(title__icontains=service_query) | Q(description__icontains=service_query))
        service_provider = ServiceProvider.objects.filter(Q(sp_name__icontains=service_query))

    return render(request, 'search_services.html', {
    'service_query': service_query,
    'services': services,
    'service_provider': service_provider,
    })   



def all_services(request):
    services = Services.objects.all()
    return render(request, 'all_services.html', {
    'services': services,

    })

# def view_service(request):
#     services = Services.objects.all()
#     serpro = ServiceProvider.objects.all()
#     return render(request, 'view_service.html', {
#     'services': services,
#     'serpro': serpro,
#     })

def view_service_category(request, service_provider_services):
    service_provider = get_object_or_404(ServiceProvider, sp_name=service_provider_services) 
    services = Services.objects.filter(status=Services.ACTIVE, service_provider=service_provider)
    return render(request, 'view_service_category.html', { 
        'service_provider': service_provider,
        'services': services,  
    })













