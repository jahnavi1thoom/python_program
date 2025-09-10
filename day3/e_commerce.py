def apply_discount(price,discount_percent):
     discounted_price=price*(discount_percent/100)
     return price-discounted_price
def add_gst(price,gst_percent=18):
     new_price=price*(gst_percent/100)
     return price+new_price
def generate_invoice(cart):
     for key,value in cart.items():
          print(key,value)

     

