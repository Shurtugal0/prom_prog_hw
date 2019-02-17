import pika
from time import sleep

sleep(10)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('172.18.0.1',
                                5672,
                                '/',
                                credentials)
)
channel = connection.channel()


channel.queue_declare(queue='numbers')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='numbers',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()