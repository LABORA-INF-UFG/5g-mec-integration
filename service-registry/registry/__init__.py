from mongoengine import connect
import os

def init_app(app):

    connect(
        db='service_registry',
        host='mongodb://adminuser:password123@10.104.4.38:27017/?authSource=admin'
    )