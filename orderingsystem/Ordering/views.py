from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Ordering


from Ordering import models
import datetime
from django.db.models import Sum

import csv

# Create your views here.


def showOrder(request):
    if request.method == 'POST':
        username = request.user

        size = request.POST['size']
        email = request.user.email
        colour = request.POST['colour']
        quantity = int(request.POST['quantity'])
        price = 1000
        withnotax = int(quantity) * int(1000)
        tax = int(quantity) * int(1000) * .13
        Total = int(withnotax) + int(tax)

        phone = request.user.first_name

        Location = request.user.last_name

        delivered_date = request.POST['delivered_date']
        v_date = datetime.datetime.strptime(delivered_date, '%Y-%m-%d')
        error_message = None

        if(not phone):

            messages.warning(request, 'contact required')
            return render(request, 'order.html', {'error_message': error_message})

        if(not Location):

            messages.warning(request, 'Location required')
            return render(request, 'order.html', {'error_message': error_message})

        if not error_message:
            if datetime.datetime.today() > v_date:
                messages.warning(request, ' Past date cannot be selected')
                return render(request, 'order.html', {'error_message': error_message})

            elif quantity <= 9:
                messages.warning(
                    request, ' Quantity less than 10 cannot be ordered')
                return render(request, 'order.html', {'error_message': error_message})

            else:
                order = Ordering(username=username, email=email, size=size, colour=colour, quantity=quantity,
                                 Total=Total, phone=phone, location=Location, delivered_date=delivered_date)
                order.save()
                messages.warning(
                    request, 'Order placed..Please Pay Advance using khalti')
                return redirect('cart')

    else:

        return render(request, 'order.html')


def showDetails(request):

    orders = Ordering.objects.all()

    countrecord = Ordering.objects.filter(delivered="NotDelivered")
    count = 0
    for search in countrecord:

        count = count + 1

    return render(request, 'orderdetails.html', {'orders': orders, 'count': count})


def compOrder(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            searchdata = Ordering.objects.filter(username__icontains=search, delivered="Delivered") or Ordering.objects.filter(
                id__icontains=search, delivered="Delivered")
            countrecord = Ordering.objects.filter(
                username=search, delivered="Delivered").count

            return render(request, 'completedorders.html', {'searchdata': searchdata, 'countrecord': countrecord})
        else:
            searchdata = Ordering.objects.filter(delivered="Delivered")
            countrecord = Ordering.objects.filter(delivered="Delivered").count

            return render(request, 'completedorders.html', {'searchdata': searchdata, 'countrecord': countrecord})

    else:

        orders = Ordering.objects.all().order_by('delivered_date')
        countrecord = Ordering.objects.filter(delivered="Delivered",).count

        return render(request, 'completedorders.html', {'orders': orders, 'countrecord': countrecord})


def edit(request, id):
    orders = Ordering.objects.get(id=id)
    return render(request, 'Orderedit.html', {'orders': orders})


def fulldetails(request, id):
    orders = Ordering.objects.get(id=id)
    order = Ordering.objects.all()
    delivery = 100
    total = orders.Total
    totalamount = int(total) + delivery - 1000
    return render(request, 'Fulldetails.html', {'orders': orders, 'order': order, 'totalamount': totalamount, 'delivery': delivery})


def update(request, id):

    if request.method == 'POST':
        phone = request.POST['phone']

        username = request.POST['username']
        size = request.POST['size']

        colour = request.POST['colour']
        quantity = request.POST['quantity']
        Total = request.POST['Total']
        phone = request.POST['phone']
        email = request.POST['email']
        Location = request.POST['location']
        delivered_date = request.POST['delivered_date']

        delivered = request.POST['delivered']
        verified = request.POST['verified']

        order = Ordering(id=id, username=username, size=size, colour=colour, quantity=quantity, Total=Total, phone=phone,
                         email=email, location=Location, delivered=delivered, verified=verified, delivered_date=delivered_date)
        order.save()
        messages.warning(request, 'Order details Updated')
        return redirect('/order/orderdetails')


def delete(request, id):
    orders = Ordering.objects.get(id=id)
    orders.delete()
    messages.warning(request, 'Order Deleted')
    return redirect('/order/orderdetails')


def deletecompleted(request, id):
    orders = Ordering.objects.get(id=id)
    orders.delete()
    messages.warning(request, 'Order Deleted')
    return redirect('/order/completedorder')


def userordersdelete(request, id):
    orders = Ordering.objects.get(id=id)
    orders.delete()
    messages.warning(request, 'Order Deleted')
    return redirect('/order/userorders')


def searchHandle(request):

    if request.method == 'POST':

        search = request.POST['search']
        date1 = str(request.POST.get('q1'))
        date2 = str(request.POST.get('q2'))
        csv1 = request.POST.get('1')
        searchdata = Ordering.objects.raw(
            'select * from Ordering_ordering where colour="'+search+'" and ordered_date between "'+date1+'" and "'+date2+'"')
        sum = 0
        countrecord = 0
        for se in searchdata:
            if se.delivered == "Delivered":
                sum = se.Total + sum
                countrecord = countrecord + 1

        if searchdata:

            if csv1:

                response = HttpResponse(content_type='text/csv')

                writer = csv.writer(response)

                writer.writerow(['Organization', 'Username', 'Size/Colour', 'Quantity',
                                 'Total Price', 'Location', 'Ordered Date', 'Delivered Date'])
                search = searchdata

                for se in search:
                    if se.delivered == "Delivered":
                        writer.writerow([se.Organization, se.username, se.size+"/"+se.colour,
                                         se.quantity, se.Total, se.location, se.ordered_date, se.delivered_date])

                writer.writerow(['Total Orders'])
                writer.writerow([countrecord])
                writer.writerow(['Total'])
                writer.writerow([sum])

                response['Content-Disposition'] = 'attachment; filename="Result.csv"'

                return response
            else:

                searchdata = Ordering.objects.raw(
                    'select * from Ordering_ordering where colour="'+search+'" and ordered_date between "'+date1+'" and "'+date2+'"')

                return render(request, 'reports.html', {'searchdata': searchdata, 'countrecord': countrecord, 'sum': sum, 'search': search})
        else:
            messages.warning(request, 'No record Found')
            return render(request, 'reports.html',)
    else:

        return render(request, 'reports.html')


def searchHandle1(request):

    if request.method == 'POST':

        search = str(request.POST['search'])
        if search:
            date1 = str(request.POST.get('q1'))
            date2 = str(request.POST.get('q2'))
            csv1 = request.POST.get('1')
            searchdata = Ordering.objects.raw(
                'select * from Ordering_ordering where username="'+search+'" and ordered_date between "'+date1+'" and "'+date2+'"')

            sum = 0
            countrecord = 0
            for se in searchdata:
                if se.delivered == "Delivered":
                    sum = se.Total + sum
                    countrecord = countrecord + 1

            if searchdata:

                if csv1:

                    response = HttpResponse(content_type='text/csv')

                    writer = csv.writer(response)

                    writer.writerow(['Username', 'Size/Colour', 'Quantity',
                                     'Total Price', 'Location', 'Ordered Date', 'Delivered Date'])
                    search = searchdata

                    for se in search:
                        if se.delivered == "Delivered":
                            writer.writerow([se.username, se.size+"/"+se.colour,
                                             se.quantity, se.Total, se.location, se.ordered_date, se.delivered_date])

                    writer.writerow(['Total Orders'])
                    writer.writerow([countrecord])
                    writer.writerow(['Total'])
                    writer.writerow([sum])

                    response['Content-Disposition'] = 'attachment; filename="Result.csv"'

                    return response

                else:

                    return render(request, 'reports.html', {'searchdata': searchdata, 'countrecord': countrecord, 'sum': sum, 'search': search, 'date1': date1, 'date2': date2})
            else:
                messages.warning(request, 'No record Found')
                return render(request, 'reports.html',)
        else:

            date1 = str(request.POST.get('q1'))
            date2 = str(request.POST.get('q2'))
            csv1 = request.POST.get('1')
            searchdata = Ordering.objects.raw(
                'select * from Ordering_ordering where ordered_date between "'+date1+'" and "'+date2+'"')

            sum = 0
            countrecord = 0
            for se in searchdata:
                if se.delivered == "Delivered":
                    sum = se.Total + sum
                    countrecord = countrecord + 1

            if searchdata:

                if csv1:

                    response = HttpResponse(content_type='text/csv')

                    writer = csv.writer(response)

                    writer.writerow(['Username', 'Size/Colour', 'Quantity',
                                     'Total Price', 'Location', 'Ordered Date', 'Delivered Date'])
                    search = searchdata
                    if search:
                        for se in search:
                            if se.delivered == "Delivered":
                                writer.writerow([se.username, se.size+"/"+se.colour,
                                                 se.quantity, se.Total, se.location, se.ordered_date, se.delivered_date])

                        writer.writerow(['Total Orders'])
                        writer.writerow([countrecord])
                        writer.writerow(['Total'])
                        writer.writerow([sum])

                        response['Content-Disposition'] = 'attachment; filename="Result.csv"'

                        return response
                    else:
                        messages.warning(request, 'No record Found')
                        return render(request, 'reports.html',)
                else:

                    return render(request, 'reports.html', {'searchdata': searchdata, 'countrecord': countrecord, 'sum': sum, 'search': search, 'date1': date1, 'date2': date2})
            else:
                messages.warning(request, 'No record Found')
                return render(request, 'reports.html',)

            return render(request, 'reports.html', {'searchdata': searchdata, 'countrecord': countrecord, 'sum': sum, 'date1': date1, 'date2': date2})

    else:

        return render(request, 'reports.html')


def showUserORder(request):
    orders = Ordering.objects.all().order_by('delivered_date')
    sum = 0
    count = 0
    countrecord = Ordering.objects.filter(
        username=request.user, delivered="Delivered")
    for search in countrecord:
        sum = search.Total + sum
        count = count + 1

    return render(request, 'myorder.html', {'orders': orders, 'count': count, 'sum': sum})


def cart(request):
    orders = Ordering.objects.all().order_by('delivered_date')
    sum = 0
    count = 0
    countrecord = Ordering.objects.filter(
        username=request.user, delivered="NotDelivered")
    for search in countrecord:
        sum = search.Total + sum
        count = count + 1

    return render(request, 'cart.html', {'orders': orders, 'count': count, 'sum': sum})


def paypal(request, id):
    orders = Ordering.objects.get(id=id)
    order = Ordering.objects.all()

    return render(request, 'paypal.html', {'orders': orders, 'order': order})


def invoice(request):

    if request.method == 'POST':

        search = request.POST['search']
        date1 = str(request.POST.get('q1'))
        searchdata = Ordering.objects.raw('select * from Ordering_ordering where username="'+search+'" and delivered_date="'+date1+'"')

        try:
            order = Ordering.objects.filter(username=search)
            username = order[0].username
            location = order[0].location
            phone = order[0].phone
            email = order[0].email
        except:
            messages.warning(request, 'No record Found to generate Invoice')
            return render(request, 'invoice.html')

        sum = 0
        for se in searchdata:
            if se.delivered == "NotDelivered":
                sum = se.Total + sum
            else:
                sum = se.Total + sum
        totalamount = sum + 200

        if searchdata:
            for se in searchdata:
                if se.delivered == "NotDelivered":
                    return render(request, 'invoicegenerated.html', {'searchdata': searchdata, 'totalamount': totalamount,
                                                                     'username': username, 'location': location, 'phone': phone, 'email': email})
                elif se.delivered == "Delivered":
                    return render(request, 'invoicegenerated.html', {'searchdata': searchdata, 'totalamount': totalamount,
                                                                     'username': username, 'location': location, 'phone': phone, 'email': email})
        else:
            messages.warning(request, 'No record Found to generate Invoice')
            return render(request, 'invoice.html')

    else:

        return render(request, 'invoice.html')
