import pika
import time
import connect
from models import Contact

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue')

    def callback(ch, method, properties, body):
        contact_id = body.decode()
        contact = Contact.objects(id=contact_id).first()

        print(f"Sending email to {contact.email}...")
        time.sleep(1)

        if not contact:
            print("Contact not found")
            return

        contact.is_sent = True
        contact.save()

        print(f"Email sent to {contact.email}")

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming()


if __name__ == "__main__":
    main()
