import connect
from models import Contact
from faker import Faker
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')




fake = Faker()

for _ in range(5):
    contact = Contact(fullname=fake.name(), email=fake.ascii_email())
    contact.save()
    channel.basic_publish(
        exchange="",
        routing_key="email_queue",
        body=str(contact.id)
    )
connection.close()






