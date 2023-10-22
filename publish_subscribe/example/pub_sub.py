from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Set

class Subscriber(ABC):

    @abstractmethod
    def update(self) -> None:
        ...

class ConcreteSubscribers(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, topic:str, message: str) -> None:
        print(f'|{topic}| {self.name} received: {message}')


class Publisher(ABC):
    topic: str
    messages: List[str] = []
    pub: Gateway

    @abstractmethod
    def publish(self, message: str) -> None:
        ...


class ConcretePublisher(ABC):
    def __init__(self, topic: str, gateway: Gateway):
        self.topic = topic
        self.gateway = gateway

    def publish(self, message: str) -> None:
        msg = {
            'topic': self.topic,
            'message': message
        }
        self.gateway.receive_message(msg)


class Gateway:
    _subscribers_by_topic: Dict[str, Set] = {}
    _queue_messages: List[Dict[str, str]] = []

    def __init__(self):
        ...

    def add_subscriber_by_topic(self, topic: str, subscriber: Subscriber) -> None:
        if topic in self._subscribers_by_topic:
            self._subscribers_by_topic[topic].add(subscriber)
        else:
            self._subscribers_by_topic[topic] = { subscriber }
    
    def receive_message(self, message: Dict[str, str]) -> None:
        self._queue_messages.append(message)
    
    def _send_message_by_topic(self, topic, message) -> None:
        for subscribe in self._subscribers_by_topic[topic]:
            subscribe.update(topic, message)
    
    def broadcast(self):
        for message in self._queue_messages:
            self._send_message_by_topic(message['topic'], message['message'])
        
        self._queue_messages = []

           
if __name__ == '__main__':
    hiago = ConcreteSubscribers('Hiago')

    gateway = Gateway()

    site_1 = ConcretePublisher('fisica', gateway)
    site_2 = ConcretePublisher('matematica', gateway)

    gateway.add_subscriber_by_topic('fisica', hiago)
    gateway.add_subscriber_by_topic('matematica', hiago)

    site_1.publish('Nova particula descoberta.')
    site_2.publish('Novo Teorema publicado.')

    gateway.broadcast()