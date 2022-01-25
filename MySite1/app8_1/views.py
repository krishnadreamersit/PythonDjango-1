from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Person
from .models import Student
from .models import Client

def crud(request):
# Save Record
    # person1 = Person(pid=1, full_name="Raj Rai", contact_address="Kthmandu")
    # person1.save()

    # person2 = Person()
    # person2.pid=2
    # person2.full_name="Kiran Rai"
    # person2.contact_address="Lalitpur"
    # person2.save()

# Select or Filter Records/Search
    # Select All
    # all_clients = Client.objects.all()
    #for client in all_clients:
        #print(client)

    # Get Value # Select * from Client where full_name='Raj'
    # clients = Client.objects.get(full_name='Raj')

    # Filter
    # result = Client.objects.filter(id=1)
    # result = Client.objects.filter(id=175)
    # result = Client.objects.filter(full_name='UTSAV')
    # result = Client.objects.filter(full_name__exact='UTSAV')
    # result = Client.objects.filter(full_name__contains='UTSAV')
    # result = Client.objects.filter(id=231, full_name__contains='UTSAV')
    # result = Client.objects.filter(contact_address__contains='DOL').filter(full_name__contains='UT')
    # result = Client.objects.all().exclude(id = 20)

    # result = Client.objects.exclude(contact_address='GORKHS')
    # result = Client.objects.exclude(id__gt=50)
    # result = Client.objects.filter(id__gt=50)
    # result = Client.objects.filter(contact_address='GORKHA')
    # result = Client.objects.filter(id__in=[2, 3])
    # result = Client.objects.filter(full_name__endswith='A')
    result = Client.objects.filter(full_name__startswith='A')

    for item in result:
        print(item)

    # Order By
    # result = Client.objects.all().order_by('id')
    # result = Client.objects.all().order_by('-id')
    # result = Client.objects.order_by('-id').order_by('full_name').order_by('-contact_address')

    # Result to Dict
    # results = Client.objects.values()
    # print(type(results))
    # print(type(results[0]))
    #return render(request, "app8_2/index.html", {'results':results})

    # Result to List
    # results = Client.objects.all()
    # print(type(results))
    # print(type(results[0]))
    # client = results[0]
    # print(type(client))
    # print(client.id, client.full_name, client.contact_address)
    # return render(request, "app8_2/index.html", {'results':results})

# Update
    # Individual Object Update
    # client = Client.objects.get(id=1)
    # client.full_name="RAJ"
    # client.contact_address="POKHARA"
    # client.save()

    # client = Client.objects.get(id=1)
    # client.full_name = "RAJ"
    # client.save()

    # client = Client.objects.get(id=1)
    # client.contact_address = "POKHARA"
    # client.save()

    # Bulk Update
    # Client.objects.select_for_update().filter(contact_address__contains='GOR').update(contact_address='PATAN')

# Delete
    # Individual Delete
    # client = Client.objects.get(id = 1)
    # client.delete()

    # Bulk Delete
    # Client.objects.select_for_update().filter(contact_address__contains='GOR').delete()
    return HttpResponse("Hello from Model CRUD")