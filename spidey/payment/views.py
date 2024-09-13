from django.shortcuts import render
from .razorpay_integration import initiate_payment,client
import razorpay

def payment_view(request,amount = 69):
   order_id = initiate_payment(amount)
   context = {
       'order_id': order_id,
       'amount': amount
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