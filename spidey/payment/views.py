from django.shortcuts import render
from .razorpay_integration import initiate_payment,client
import razorpay
from .models import Order
from base.models import Stamp


def payment_view(request, pk):
   # Set the amount dynamically or based on your requirements
   stamp = Stamp.objects.get(pk=pk)
   order_id = initiate_payment(int(stamp.price))
   order = Order.objects.create(stamp=stamp, provider_order_id=order_id)
   context = {
       'order': order
   }
   return render(request, 'payment.html', context)


def payment_success_view(request):
   order_id = request.POST.get('order_id')
   payment_id = request.POST.get('razorpay_payment_id')
   signature = request.POST.get('razorpay_signature')
   params_dict = {
       'razorpay_order_id': order_id,
       'razorpay_payment_id': payment_id,
       'razorpay_signature': signature
   }
   try:
       client.utility.verify_payment_signature(params_dict)
       # Payment signature verification successful
       # Perform any required actions (e.g., update the order status)
       return render(request, 'payment_success.html')
   except razorpay.errors.SignatureVerificationError as e:
       # Payment signature verification failed
       # Handle the error accordingly
       return render(request, 'payment_failure.html')