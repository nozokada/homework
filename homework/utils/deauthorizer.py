from uplink import Consumer


class Deauthorizer:

    def __init__(self, consumer: Consumer):
        self.consumer = consumer

    def __enter__(self):
        self.token = self.consumer.session.headers.pop('Authorization')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.consumer.session.headers['Authorization'] = self.token
