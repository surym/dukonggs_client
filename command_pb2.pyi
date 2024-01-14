from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CommandMessage(_message.Message):
    __slots__ = ("gameType", "session", "content")
    GAMETYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    gameType: str
    session: str
    content: str
    def __init__(self, gameType: _Optional[str] = ..., session: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class StartGameRequest(_message.Message):
    __slots__ = ("name", "gameType")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GAMETYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    gameType: str
    def __init__(self, name: _Optional[str] = ..., gameType: _Optional[str] = ...) -> None: ...

class StartGameReply(_message.Message):
    __slots__ = ("success", "session", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    session: str
    message: str
    def __init__(self, success: bool = ..., session: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class StopGameRequest(_message.Message):
    __slots__ = ("name", "gameType", "session", "content")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GAMETYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    gameType: str
    session: str
    content: str
    def __init__(self, name: _Optional[str] = ..., gameType: _Optional[str] = ..., session: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class StopGameReply(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class ChatMessage(_message.Message):
    __slots__ = ("name", "message")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    message: str
    def __init__(self, name: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
