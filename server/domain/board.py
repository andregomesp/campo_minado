from typing import List, Type
from domain.bomb import Bomb


class Board:
    bombs = List[Type[Bomb]]

