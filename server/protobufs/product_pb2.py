# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobufs/product.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17protobufs/product.proto\"\x07\n\x05\x45mpty\"\x1b\n\rProductItemId\x12\n\n\x02id\x18\x01 \x01(\x05\"2\n\x07NewItem\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\"6\n\x0bProductItem\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\"-\n\x0bProductList\x12\x1e\n\x08Products\x18\x01 \x03(\x0b\x32\x0c.ProductItem2\xa6\x01\n\x0eProductService\x12\x1e\n\x04List\x12\x06.Empty\x1a\x0c.ProductList\"\x00\x12\"\n\x06Insert\x12\x08.NewItem\x1a\x0c.ProductItem\"\x00\x12&\n\x04\x46ind\x12\x0e.ProductItemId\x1a\x0c.ProductItem\"\x00\x12(\n\x06\x44\x65lete\x12\x0e.ProductItemId\x1a\x0c.ProductItem\"\x00\x62\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_PRODUCTITEMID = DESCRIPTOR.message_types_by_name['ProductItemId']
_NEWITEM = DESCRIPTOR.message_types_by_name['NewItem']
_PRODUCTITEM = DESCRIPTOR.message_types_by_name['ProductItem']
_PRODUCTLIST = DESCRIPTOR.message_types_by_name['ProductList']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'protobufs.product_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

ProductItemId = _reflection.GeneratedProtocolMessageType('ProductItemId', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTITEMID,
  '__module__' : 'protobufs.product_pb2'
  # @@protoc_insertion_point(class_scope:ProductItemId)
  })
_sym_db.RegisterMessage(ProductItemId)

NewItem = _reflection.GeneratedProtocolMessageType('NewItem', (_message.Message,), {
  'DESCRIPTOR' : _NEWITEM,
  '__module__' : 'protobufs.product_pb2'
  # @@protoc_insertion_point(class_scope:NewItem)
  })
_sym_db.RegisterMessage(NewItem)

ProductItem = _reflection.GeneratedProtocolMessageType('ProductItem', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTITEM,
  '__module__' : 'protobufs.product_pb2'
  # @@protoc_insertion_point(class_scope:ProductItem)
  })
_sym_db.RegisterMessage(ProductItem)

ProductList = _reflection.GeneratedProtocolMessageType('ProductList', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTLIST,
  '__module__' : 'protobufs.product_pb2'
  # @@protoc_insertion_point(class_scope:ProductList)
  })
_sym_db.RegisterMessage(ProductList)

_PRODUCTSERVICE = DESCRIPTOR.services_by_name['ProductService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=27
  _EMPTY._serialized_end=34
  _PRODUCTITEMID._serialized_start=36
  _PRODUCTITEMID._serialized_end=63
  _NEWITEM._serialized_start=65
  _NEWITEM._serialized_end=115
  _PRODUCTITEM._serialized_start=117
  _PRODUCTITEM._serialized_end=171
  _PRODUCTLIST._serialized_start=173
  _PRODUCTLIST._serialized_end=218
  _PRODUCTSERVICE._serialized_start=221
  _PRODUCTSERVICE._serialized_end=387
# @@protoc_insertion_point(module_scope)
