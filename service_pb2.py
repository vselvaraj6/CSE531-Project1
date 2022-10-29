# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"\x18\n\x06Output\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x18\n\nQueryInput\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1c\n\x0bQueryOutput\x12\r\n\x05money\x18\x01 \x01(\x03\")\n\x0c\x44\x65positInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"*\n\rWithdrawInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"3\n\x16PropogateWithdrawInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"2\n\x15PropogateDepositInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\x32\xe0\x01\n\x06\x42ranch\x12\"\n\x05Query\x12\x0b.QueryInput\x1a\x0c.QueryOutput\x12!\n\x07\x44\x65posit\x12\r.DepositInput\x1a\x07.Output\x12#\n\x08Withdraw\x12\x0e.WithdrawInput\x1a\x07.Output\x12\x35\n\x11PropogateWithdraw\x12\x17.PropogateWithdrawInput\x1a\x07.Output\x12\x33\n\x10PropogateDeposit\x12\x16.PropogateDepositInput\x1a\x07.Outputb\x06proto3')



_OUTPUT = DESCRIPTOR.message_types_by_name['Output']
_QUERYINPUT = DESCRIPTOR.message_types_by_name['QueryInput']
_QUERYOUTPUT = DESCRIPTOR.message_types_by_name['QueryOutput']
_DEPOSITINPUT = DESCRIPTOR.message_types_by_name['DepositInput']
_WITHDRAWINPUT = DESCRIPTOR.message_types_by_name['WithdrawInput']
_PROPOGATEWITHDRAWINPUT = DESCRIPTOR.message_types_by_name['PropogateWithdrawInput']
_PROPOGATEDEPOSITINPUT = DESCRIPTOR.message_types_by_name['PropogateDepositInput']
Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Output)
  })
_sym_db.RegisterMessage(Output)

QueryInput = _reflection.GeneratedProtocolMessageType('QueryInput', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:QueryInput)
  })
_sym_db.RegisterMessage(QueryInput)

QueryOutput = _reflection.GeneratedProtocolMessageType('QueryOutput', (_message.Message,), {
  'DESCRIPTOR' : _QUERYOUTPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:QueryOutput)
  })
_sym_db.RegisterMessage(QueryOutput)

DepositInput = _reflection.GeneratedProtocolMessageType('DepositInput', (_message.Message,), {
  'DESCRIPTOR' : _DEPOSITINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:DepositInput)
  })
_sym_db.RegisterMessage(DepositInput)

WithdrawInput = _reflection.GeneratedProtocolMessageType('WithdrawInput', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:WithdrawInput)
  })
_sym_db.RegisterMessage(WithdrawInput)

PropogateWithdrawInput = _reflection.GeneratedProtocolMessageType('PropogateWithdrawInput', (_message.Message,), {
  'DESCRIPTOR' : _PROPOGATEWITHDRAWINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:PropogateWithdrawInput)
  })
_sym_db.RegisterMessage(PropogateWithdrawInput)

PropogateDepositInput = _reflection.GeneratedProtocolMessageType('PropogateDepositInput', (_message.Message,), {
  'DESCRIPTOR' : _PROPOGATEDEPOSITINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:PropogateDepositInput)
  })
_sym_db.RegisterMessage(PropogateDepositInput)

_BRANCH = DESCRIPTOR.services_by_name['Branch']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OUTPUT._serialized_start=17
  _OUTPUT._serialized_end=41
  _QUERYINPUT._serialized_start=43
  _QUERYINPUT._serialized_end=67
  _QUERYOUTPUT._serialized_start=69
  _QUERYOUTPUT._serialized_end=97
  _DEPOSITINPUT._serialized_start=99
  _DEPOSITINPUT._serialized_end=140
  _WITHDRAWINPUT._serialized_start=142
  _WITHDRAWINPUT._serialized_end=184
  _PROPOGATEWITHDRAWINPUT._serialized_start=186
  _PROPOGATEWITHDRAWINPUT._serialized_end=237
  _PROPOGATEDEPOSITINPUT._serialized_start=239
  _PROPOGATEDEPOSITINPUT._serialized_end=289
  _BRANCH._serialized_start=292
  _BRANCH._serialized_end=516
# @@protoc_insertion_point(module_scope)
