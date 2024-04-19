from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentDetails(_message.Message):
    __slots__ = ("project_id",)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ("data_id", "data_elements")
    DATA_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    data_id: str
    data_elements: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, data_id: _Optional[str] = ..., data_elements: _Optional[_Iterable[str]] = ...) -> None: ...
