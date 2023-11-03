from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import random
class PaymentView(View):
    
    def get(self, request):
        return render(request, 'home.html')
    
    def post(self, request):
        try:
            amount = request.POST.get('amount')
            data = payment_function(amount)
            url = data['data']
            return redirect(url['payment_url'])
        except Exception as e:
            raise e
        # url = data['payment_url']
        return url
        return render(request, 'home.html')
        
    

def payment_function(amount):
    url = 'https://api.ekqr.in/api/create_order'
    data = {
            "key": settings.PAYMENT_KEY,
            "client_txn_id": random.randint(100000,999999), #unique id
            "amount": amount,
            "p_info": "Product Name",
            "customer_name": "Jon Doe",
            "customer_email": "jondoe@gmail.com",
            "customer_mobile": "9876543210",
            "redirect_url": "http://google.com",
            "udf1": "user defined field 1 (max 25 char)",
            "udf2": "user defined field 2 (max 25 char)",
            "udf3": "user defined field 3 (max 25 char)"
        }
    
    response = requests.post(url=url, data=data)
    return response.json()


class PaymentAPIView(APIView):
    
    def post(self, request):
        data = request.data
        print("********", data)
        data_new = payment_function(data.get('amount'))
        print("&&&&&&&&&&&", data_new)
        return Response(data=data_new, status=200)
