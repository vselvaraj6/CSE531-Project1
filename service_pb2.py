# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"3\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1c\n\x05\x65vent\x18\x03 \x01(\x0b\x32\r.EventRequest\")\n\x16PropogateBranchRequest\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x05\"H\n\x0c\x45ventRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1d\n\tinterface\x18\x02 \x01(\x0e\x32\n.Interface\x12\r\n\x05money\x18\x03 \x01(\x05\"_\n\x19UpdateTransactionResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1d\n\tinterface\x18\x02 \x01(\x0e\x32\n.Interface\x12\x17\n\x06result\x18\x03 \x01(\x0e\x32\x07.Result\"l\n\x17ReadTransactionResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1d\n\tinterface\x18\x02 \x01(\x0e\x32\n.Interface\x12\r\n\x05money\x18\x03 \x01(\x05\x12\x17\n\x06result\x18\x04 \x01(\x0e\x32\x07.Result\"2\n\x17PropogateBranchResponse\x12\x17\n\x06result\x18\x01 \x01(\x0e\x32\x07.Result*.\n\x06Result\x12\n\n\x06uknown\x10\x00\x12\x0b\n\x07success\x10\x01\x12\x0b\n\x07\x66\x61ilure\x10\x02*@\n\tInterface\x12\r\n\tundefined\x10\x00\x12\x0b\n\x07\x64\x65posit\x10\x01\x12\x0c\n\x08withdraw\x10\x02\x12\t\n\x05query\x10\x03\x32\xc0\x01\n\x06\x42ranch\x12\x39\n\x11UpdateTransaction\x12\x08.Request\x1a\x1a.UpdateTransactionResponse\x12\x35\n\x0fReadTransaction\x12\x08.Request\x1a\x18.ReadTransactionResponse\x12\x44\n\x0fPropogateBranch\x12\x17.PropogateBranchRequest\x1a\x18.PropogateBranchResponseb\x06proto3')

_RESULT = DESCRIPTOR.enum_types_by_name['Result']
Result = enum_type_wrapper.EnumTypeWrapper(_RESULT)
_INTERFACE = DESCRIPTOR.enum_types_by_name['Interface']
Interface = enum_type_wrapper.EnumTypeWrapper(_INTERFACE)
uknown = 0
success = 1
failure = 2
undefined = 0
deposit = 1
withdraw = 2
query = 3


_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_PROPOGATEBRANCHREQUEST = DESCRIPTOR.message_types_by_name['PropogateBranchRequest']
_EVENTREQUEST = DESCRIPTOR.message_types_by_name['EventRequest']
_UPDATETRANSACTIONRESPONSE = DESCRIPTOR.message_types_by_name['UpdateTransactionResponse']
_READTRANSACTIONRESPONSE = DESCRIPTOR.message_types_by_name['ReadTransactionResponse']
_PROPOGATEBRANCHRESPONSE = DESCRIPTOR.message_types_by_name['PropogateBranchResponse']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

PropogateBranchRequest = _reflection.GeneratedProtocolMessageType('PropogateBranchRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROPOGATEBRANCHREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:PropogateBranchRequest)
  })
_sym_db.RegisterMessage(PropogateBranchRequest)

EventRequest = _reflection.GeneratedProtocolMessageType('EventRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:EventRequest)
  })
_sym_db.RegisterMessage(EventRequest)

UpdateTransactionResponse = _reflection.GeneratedProtocolMessageType('UpdateTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETRANSACTIONRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:UpdateTransactionResponse)
  })
_sym_db.RegisterMessage(UpdateTransactionResponse)

ReadTransactionResponse = _reflection.GeneratedProtocolMessageType('ReadTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _READTRANSACTIONRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:ReadTransactionResponse)
  })
_sym_db.RegisterMessage(ReadTransactionResponse)

PropogateBranchResponse = _reflection.GeneratedProtocolMessageType('PropogateBranchResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROPOGATEBRANCHRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:PropogateBranchResponse)
  })
_sym_db.RegisterMessage(PropogateBranchResponse)

_BRANCH = DESCRIPTOR.services_by_name['Branch']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESULT._serialized_start=446
  _RESULT._serialized_end=492
  _INTERFACE._serialized_start=494
  _INTERFACE._serialized_end=558
  _REQUEST._serialized_start=17
  _REQUEST._serialized_end=68
  _PROPOGATEBRANCHREQUEST._serialized_start=70
  _PROPOGATEBRANCHREQUEST._serialized_end=111
  _EVENTREQUEST._serialized_start=113
  _EVENTREQUEST._serialized_end=185
  _UPDATETRANSACTIONRESPONSE._serialized_start=187
  _UPDATETRANSACTIONRESPONSE._serialized_end=282
  _READTRANSACTIONRESPONSE._serialized_start=284
  _READTRANSACTIONRESPONSE._serialized_end=392
  _PROPOGATEBRANCHRESPONSE._serialized_start=394
  _PROPOGATEBRANCHRESPONSE._serialized_end=444
  _BRANCH._serialized_start=561
  _BRANCH._serialized_end=753
# @@protoc_insertion_point(module_scope)
