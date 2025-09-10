import e_commerce
d={"Laptop": 55000,"phone":30000,"headphones":2000}
sub_total=0
e_commerce.generate_invoice(d)
for i in d.values():
    sub_total+=i
print("subtotal:",sub_total)
print("after 10% discount:",e_commerce.apply_discount(sub_total,10))
print("after 18% gst:",e_commerce.add_gst(sub_total,18))



