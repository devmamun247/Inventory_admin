from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from .models import Customer, CustomerImageMany
from datetime import date,datetime


def insert (req):
    current_date = date.today()
    current_year = str(current_date.year)
    #print(type(current_year))
    name = req.POST.get('name')
    first_two_letter = name[0:2]
    # print(first_two_letter)
    # print(len(name))
    # print(name[0])
    # print((name[1]))
    designation = req.POST.get('designation')
    phone = req.POST.get('phone')
    custom_id = first_two_letter+current_year+phone
    # print(custom_id)
    email = req.POST.get('email')
    linkedin = req.POST.get('linkedin')
    fb = req.POST.get('fb')
    country = req.POST.get('country')
    address = req.POST.get('address')
    dob = req.POST.get('dob')
    image = req.FILES.get('image') 

    # Handle multiple files
    imagesmultiple = req.FILES.getlist('image_many')  # getlist will get all the files uploaded

    # Save customer object
    cust_obj = Customer(
        custom_id=custom_id,
        name=name,
        designation=designation,
        phone=phone,
        email=email,
        linkedin=linkedin,
        facebook=fb,
        country=country,
        address=address,
        dob=dob,
        image = image 
    )
    cust_obj.save()

# Save each image and associate with the customer
    for img in imagesmultiple:
        customer_image = CustomerImageMany(image_many=img)
        customer_image.save()
        cust_obj.image_many.add(customer_image)  # Add image to the customer

    #return redirect('task_upload_url_submit')

    return redirect('show_customer_data')

    # this is one process to create object
    # cust_obj =Customer()
    # cust_obj.custom_id=custom_id
    # cust_obj.name = name
    # cust_obj.designation = designation
    # cust_obj.phone = phone
    # cust_obj.email = email
    # cust_obj.linkedin = linkedin
    # cust_obj.facebook = fb
    # cust_obj.country = country
    # cust_obj.address = address
    # cust_obj.dob = dob 
    # cust_obj.image = image 
    # cust_obj.save()

    ## return HttpResponse(name)
    ## return render(req, 'task_upload.html')
    #return redirect('task_upload_url_submit')


def customer_update (req):
    uid = req.POST.get('id')
    name = req.POST.get('name')
    designation = req.POST.get('designation')
    phone = req.POST.get('phone')
    custom_id = req.POST.get('custom_id')
    email = req.POST.get('email')
    linkedin = req.POST.get('linkedin')
    fb = req.POST.get('fb')
    country = req.POST.get('country')
    address = req.POST.get('address')
    dob1 = req.POST.get('dob')
    dob = str(dob1)

    image = req.FILES.get('image') 


    # Save customer object
    cust_obj = get_object_or_404(Customer, id=uid)
    cust_obj.custom_id=custom_id,
    cust_obj.name=name,
    cust_obj.designation=designation,
    cust_obj.phone=phone,
    cust_obj.email=email,
    cust_obj.linkedin=linkedin,
    cust_obj.facebook=fb,
    cust_obj.country=country,
    cust_obj.address=address,
    cust_obj.dob=dob,
    cust_obj.image = image 
    
    cust_obj.save()

    # Handle multiple files
    imagesmultiple = req.FILES.getlist('image_many')  # getlist will get all the files uploaded

    # Save each image and associate with the customer
    for img in imagesmultiple:
        customer_image = CustomerImageMany(image_many=img)
        customer_image.save()
        cust_obj.image_many.add(customer_image)  # Add image to the customer

    return redirect('task_upload_url_submit')

def edit_customer(req,uid):
    single_instance_get_data =Customer.objects.get(id=uid) # here id is customer table column id 
    # print(single_instance_get_data.name)
    data = {"d": single_instance_get_data}
    # return HttpResponse(id)
    return render(req, 'edit_customer.html', data)


def show(req):
    customer_data = Customer.objects.all() # select * from customer
    data = {'d': customer_data}

    # Debugging: check that customer data is being passed properly
    for i in customer_data:
    #     print(i)
         #print(i.name)
         print(f"Name: {i.name}, Image: {i.image.url if i.image else 'No image'}")
    return render(req,'task_upload.html', data)
    # return HttpResponse("this is customer data")



def index (req):
    return render(req, 'task_upload.html')

# def index (req):
#     a = 10
#     b =20 
#     sum = a+b1
#     #return HttpResponse (sum)
#     return render(req, 'index.html')

