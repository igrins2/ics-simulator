# -*- coding: utf-8 -*-

"""
"""
import pika

# ics -> dcs gui consumer
# ics <- dcs core producer

class MsgMiddleware:
    def __init__(self, ip_addr, exchange, excType, isConsumer=True, port=None):
        # RabbitMQ communication
        self._ipaddr = ip_addr
        self._exchange = exchange
        self._excType = excType
        self._port = (port) if (port) else 5672
        print(self._port)
        self._connection = None 
        self._channel = None
        self._isConsumer = isConsumer
        self._queueName = None


    def __del__(self):
        print ('Closing rabbitmq queue and connections ')
        self.closeConnection()
        self._channel.stop_consuming()

    def closeConnection(self):
        if (self._isConsumer):
            self._
        self._connection.close()
           
    def connectServer(self):
       try: 
          self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._ipaddr, port=self._port))
          self._channel = self._connection.channel()
          self.declareExchange()

       except Exception as ex:
           print("Cannot connect to RabbitMQ server.\r\nPlease check the server and try again!")
           print (ex)
           raise 

    def declareExchange(self):
        try:
           self._channel.exchange_declare(exchange=self._exchange, exchange_type=self._excType) 
        except Exception as e:
           print("Can not declare the exchange.\r\nPlease check the server and try again!")
           print (e)
           raise
    
    # as consumer
    def consumer(self, routeKeys, callback):
       try:
          if (self._queueName is None):
             result = self._channel.queue_declare(queue='', exclusive=True)
             self._queueName = result.method.queue
          print(f"queueName= {self._queueName}")
          for rkey in routeKeys:
              self._channel.queue_bind(exchange=self._exchange, queue=self._queueName, routing_key=rkey)
          self._channel.basic_consume(queue=self._queueName, on_message_callback=callback, auto_ack=True)

       except Exception as e:
          print("Cannot define consumer for the {routeKey} provider.")
          print(e)
          raise 

    def startConsumer(self):
        try:
            self._channel.start_consuming()
        except Exception as e:
            print("Error starting consuming msg")
            print(e)
            raise
    
    # as producer
    def sendMessage(self, routeKeys,  message):
        try:
            for rKey in routeKeys:
                self._channel.basic_publish(exchange=self._exchange, routing_key=rKey, body=message)
        except Exception as e:
            print("Cannot send the {message} for the {routeKeys} provider.")
            print(e)
            raise

    

        
