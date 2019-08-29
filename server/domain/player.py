from server.connection.session import Session
from typing import Type


class Player:
    score: int
    session: Type[Session]
