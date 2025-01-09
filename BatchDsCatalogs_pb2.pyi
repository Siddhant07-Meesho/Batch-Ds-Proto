from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatchDsCatalogs(_message.Message):
    __slots__ = ("catalogs",)
    CATALOGS_FIELD_NUMBER: _ClassVar[int]
    catalogs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, catalogs: _Optional[_Iterable[int]] = ...) -> None: ...
