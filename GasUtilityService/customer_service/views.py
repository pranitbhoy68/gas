from django.shortcuts import render, redirect
from .models import ServiceRequest, Customer
from django.http import Http404


def submit_service_request(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        request_type = request.POST.get('request_type')
        details = request.POST.get('details')
        attachment = request.FILES.get('attachment')

        new_request = ServiceRequest.objects.create(
            customer_name=customer_name,
            request_type=request_type,
            details=details,
            attachment=attachment
        )

        return redirect('request_detail', request_id=new_request.id)

    return render(request, 'submit_service_request.html')


def request_detail(request, request_id):
    try:
        service_request = ServiceRequest.objects.get(pk=request_id)
    except ServiceRequest.DoesNotExist:
        raise Http404("Service request does not exist")

    return render(request, 'request_detail.html', {'service_request': service_request})