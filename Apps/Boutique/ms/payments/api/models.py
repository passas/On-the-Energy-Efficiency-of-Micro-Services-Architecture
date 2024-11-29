from django.db import models



class Payment (models.Model):
    order_id = models.IntegerField ()
    method = models.ForeignKey ("PaymentMethod", on_delete=models.PROTECT, related_name="how")
    processes = models.DateTimeField (auto_now_add=True)

class PaymentMethod (models.Model):
    METHOD = [
        ("PAYPAL", "PayPal"),
        ("VISA", "Visa"),
        ("GIFT CARD", "Gift Card"),
        ("OTHER", "Other"),
    ]
    method = models.CharField(max_length=16, choices=METHOD, unique=True)

    def __str__ (self):
        return f"{self.method}"
    
    def save (self, *args, **kwargs):
        error = False

        # Method
        _method = {
            "PAYPAL": "PayPal",
            "VISA": "Visa",
            "GIFT CARD": "Gift Card",
        }

        if self.method.upper() in _method:
            self.method = _method[self.method.upper()]
        else:
            self.method = "Other"
        
        # DB
        if error == False:
            super(PaymentMethod, self).save(*args, **kwargs)