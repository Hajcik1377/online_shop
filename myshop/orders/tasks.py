from celery import tasks
from django.core.mail import send_mail
from .models import Order

@tasks
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Zamówienie nr {}'.format(order.id)
    message = 'Witaj, {}!\n\Złożyłeś zamówienie w naszym sklepie.\
                Identyfikator zamówienia to {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent