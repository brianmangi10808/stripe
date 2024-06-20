# from flask import Flask,request
# import stripe

# app = Flask(__name__)
# stripe.api_key = 'sk_test_51PSj3NP8d7LUbLVe3J0NNDhjoMRyA1GcV2opveLgeR7mTiHQewcgrNGIUMgKq3fYrMsYih1hXJudXCiMqx3CGxYL006ewHIqiJ'

# @app.route('/pay')
# def pay():
#      email = request.json.get('email', None)

#      if not email:
#         return 'You need to send an Email!', 400
     
#      intent = stripe.PaymentIntent.create(
#         amount=5000,
#         currency='usd',
#         receipt_email=email
#     )
     
#      return 