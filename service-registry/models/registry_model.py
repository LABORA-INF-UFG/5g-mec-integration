from mongoengine import StringField, Document

class Registry (Document):
    service_ip = StringField()
    service_name = StringField()
    service_port = StringField()
    service_endPoint_Post = StringField()
    service_endPoint_Get = StringField() 
    service_endPoint_Put = StringField()
    service_endpoint_Delete = StringField()