import pika
from random import randint
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
channel.confirm_delivery()

while True:
    data = str(randint(1, 10000))

    if channel.basic_publish(exchange='',
                        routing_key='numbers',
                        body=data):
        print('Message has been delivered')
    else:
        print('Message not delivered')

    sleep(randint(1, 10))