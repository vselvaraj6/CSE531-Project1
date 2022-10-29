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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x04\x62\x61nk\"\x18\n\x06Output\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x18\n\nQueryInput\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1c\n\x0bQueryOutput\x12\r\n\x05money\x18\x01 \x01(\x03\")\n\x0c\x44\x65positInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"*\n\rWithdrawInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"3\n\x16PropogateWithdrawInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"2\n\x15PropogateDepositInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\x32\x92\x02\n\x06\x42ranch\x12,\n\x05Query\x12\x10.bank.QueryInput\x1a\x11.bank.QueryOutput\x12+\n\x07\x44\x65posit\x12\x12.bank.DepositInput\x1a\x0c.bank.Output\x12-\n\x08Withdraw\x12\x13.bank.WithdrawInput\x1a\x0c.bank.Output\x12?\n\x11PropogateWithdraw\x12\x1c.bank.PropogateWithdrawInput\x1a\x0c.bank.Output\x12=\n\x10PropogateDeposit\x12\x1b.bank.PropogateDepositInput\x1a\x0c.bank.Outputb\x06proto3')



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
  # @@protoc_insertion_point(class_scope:bank.Output)
  })
_sym_db.RegisterMessage(Output)

QueryInput = _reflection.GeneratedProtocolMessageType('QueryInput', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bank.QueryInput)
  })
_sym_db.RegisterMessage(QueryInput)

QueryOutput = _reflection.GeneratedProtocolMessageType('QueryOutput', (_message.Message,), {
  'DESCRIPTOR' : _QUERYOUTPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bank.QueryOutput)
  })
_sym_db.RegisterMessage(QueryOutput)

DepositInput = _reflection.GeneratedProtocolMessageType('DepositInput', (_message.Message,), {
  'DESCRIPTOR' : _DEPOSITINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bank.DepositInput)
  })
_sym_db.RegisterMessage(DepositInput)

WithdrawInput = _reflection.GeneratedProtocolMessageType('WithdrawInput', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bank.WithdrawInput)
  })
_sym_db.RegisterMessage(WithdrawInput)

PropogateWithdrawInput = _reflection.GeneratedProtocolMessageType('PropogateWithdrawInput', (_message.Message,), {
  'DESCRIPTOR' : _PROPOGATEWITHDRAWINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bank.PropogateWithdrawInput)
  })
_sym_db.RegisterMessage(PropogateWithdrawInput)

PropogateDepositInput = _reflection.GeneratedProtocolMessageType('PropogateDepositInput', (_message.Message,), {
  'DESCRIPTOR' : _PROPOGATEDEPOSITINPUT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:bank.PropogateDepositInput)
  })
_sym_db.RegisterMessage(PropogateDepositInput)

_BRANCH = DESCRIPTOR.services_by_name['Branch']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OUTPUT._serialized_start=23
  _OUTPUT._serialized_end=47
  _QUERYINPUT._serialized_start=49
  _QUERYINPUT._serialized_end=73
  _QUERYOUTPUT._serialized_start=75
  _QUERYOUTPUT._serialized_end=103
  _DEPOSITINPUT._serialized_start=105
  _DEPOSITINPUT._serialized_end=146
  _WITHDRAWINPUT._serialized_start=148
  _WITHDRAWINPUT._serialized_end=190
  _PROPOGATEWITHDRAWINPUT._serialized_start=192
  _PROPOGATEWITHDRAWINPUT._serialized_end=243
  _PROPOGATEDEPOSITINPUT._serialized_start=245
  _PROPOGATEDEPOSITINPUT._serialized_end=295
  _BRANCH._serialized_start=298
  _BRANCH._serialized_end=572
# @@protoc_insertion_point(module_scope)
