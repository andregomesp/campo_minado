from typing import List, Type
from server.domain.bomb import Bomb


class Board:
    bombs = List[Type[Bomb]]

