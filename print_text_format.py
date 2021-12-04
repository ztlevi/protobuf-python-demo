#!/usr/bin/env python3
from google.protobuf import text_format

import addressbook_pb2

# message = my_proto_pb2.MyMessage(foo='bar')
person = addressbook_pb2.Person(name="Alice", id=1, email="alice@sample.com")
phone_number = person.phones.add()
phone_number.type = addressbook_pb2.Person.PhoneType.MOBILE
phone_number.number = "111111"

text_proto = text_format.MessageToString(person)

# Parse a text proto string.
person_read = text_format.Parse(text_proto, addressbook_pb2.Person())
