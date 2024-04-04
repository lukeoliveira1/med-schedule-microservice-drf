# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: appointments/grpc/appointments.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$appointments/grpc/appointments.proto\x12\x15settings.appointments\x1a\x1bgoogle/protobuf/empty.proto\"\'\n\x19\x41ppointmentDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x18\n\x16\x41ppointmentListRequest\"e\n\x17\x41ppointmentListResponse\x12;\n\x07results\x18\x01 \x03(\x0b\x32*.settings.appointments.AppointmentResponse\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"\xa7\x01\n\x1f\x41ppointmentPartialUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tdoctor_id\x18\x02 \x01(\x05\x12\x12\n\npatient_id\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x10\n\x08symptoms\x18\x05 \x01(\t\x12\x11\n\tdiagnosis\x18\x06 \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\x07 \x03(\t\"z\n\x12\x41ppointmentRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tdoctor_id\x18\x02 \x01(\x05\x12\x12\n\npatient_id\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x10\n\x08symptoms\x18\x05 \x01(\t\x12\x11\n\tdiagnosis\x18\x06 \x01(\t\"{\n\x13\x41ppointmentResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tdoctor_id\x18\x02 \x01(\x05\x12\x12\n\npatient_id\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x10\n\x08symptoms\x18\x05 \x01(\t\x12\x11\n\tdiagnosis\x18\x06 \x01(\t\"(\n\x1a\x41ppointmentRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x81\x05\n\x15\x41ppointmentController\x12\x61\n\x06\x43reate\x12).settings.appointments.AppointmentRequest\x1a*.settings.appointments.AppointmentResponse\"\x00\x12U\n\x07\x44\x65stroy\x12\x30.settings.appointments.AppointmentDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12g\n\x04List\x12-.settings.appointments.AppointmentListRequest\x1a..settings.appointments.AppointmentListResponse\"\x00\x12u\n\rPartialUpdate\x12\x36.settings.appointments.AppointmentPartialUpdateRequest\x1a*.settings.appointments.AppointmentResponse\"\x00\x12k\n\x08Retrieve\x12\x31.settings.appointments.AppointmentRetrieveRequest\x1a*.settings.appointments.AppointmentResponse\"\x00\x12\x61\n\x06Update\x12).settings.appointments.AppointmentRequest\x1a*.settings.appointments.AppointmentResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'appointments.grpc.appointments_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_APPOINTMENTDESTROYREQUEST']._serialized_start=92
  _globals['_APPOINTMENTDESTROYREQUEST']._serialized_end=131
  _globals['_APPOINTMENTLISTREQUEST']._serialized_start=133
  _globals['_APPOINTMENTLISTREQUEST']._serialized_end=157
  _globals['_APPOINTMENTLISTRESPONSE']._serialized_start=159
  _globals['_APPOINTMENTLISTRESPONSE']._serialized_end=260
  _globals['_APPOINTMENTPARTIALUPDATEREQUEST']._serialized_start=263
  _globals['_APPOINTMENTPARTIALUPDATEREQUEST']._serialized_end=430
  _globals['_APPOINTMENTREQUEST']._serialized_start=432
  _globals['_APPOINTMENTREQUEST']._serialized_end=554
  _globals['_APPOINTMENTRESPONSE']._serialized_start=556
  _globals['_APPOINTMENTRESPONSE']._serialized_end=679
  _globals['_APPOINTMENTRETRIEVEREQUEST']._serialized_start=681
  _globals['_APPOINTMENTRETRIEVEREQUEST']._serialized_end=721
  _globals['_APPOINTMENTCONTROLLER']._serialized_start=724
  _globals['_APPOINTMENTCONTROLLER']._serialized_end=1365
# @@protoc_insertion_point(module_scope)
