# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x18\n\nQueryInput\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1c\n\x0bQueryOutput\x12\r\n\x05money\x18\x01 \x01(\x03\")\n\x0c\x44\x65positInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"*\n\rWithdrawInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"3\n\x16PropogateWithdrawInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\"2\n\x15PropogateDepositInput\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05money\x18\x02 \x01(\x03\x32\xa6\x02\n\x06\x42ranch\x12$\n\x05Query\x12\x0b.QueryInput\x1a\x0c.QueryOutput\"\x00\x12\x32\n\x07\x44\x65posit\x12\r.DepositInput\x1a\x16.google.protobuf.Empty\"\x00\x12\x34\n\x08Withdraw\x12\x0e.WithdrawInput\x1a\x16.google.protobuf.Empty\"\x00\x12\x46\n\x11PropogateWithdraw\x12\x17.PropogateWithdrawInput\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\x10PropogateDeposit\x12\x16.PropogateDepositInput\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUERYINPUT._serialized_start=46
  _QUERYINPUT._serialized_end=70
  _QUERYOUTPUT._serialized_start=72
  _QUERYOUTPUT._serialized_end=100
  _DEPOSITINPUT._serialized_start=102
  _DEPOSITINPUT._serialized_end=143
  _WITHDRAWINPUT._serialized_start=145
  _WITHDRAWINPUT._serialized_end=187
  _PROPOGATEWITHDRAWINPUT._serialized_start=189
  _PROPOGATEWITHDRAWINPUT._serialized_end=240
  _PROPOGATEDEPOSITINPUT._serialized_start=242
  _PROPOGATEDEPOSITINPUT._serialized_end=292
  _BRANCH._serialized_start=295
  _BRANCH._serialized_end=589
# @@protoc_insertion_point(module_scope)
