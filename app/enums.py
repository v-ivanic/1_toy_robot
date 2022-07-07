import enum


class FACING(str, enum.Enum):
    NORTH = "NORTH",
    WEST = "WEST",
    SOUTH = "SOUTH",
    EAST = "EAST"


class STATE_KEYS(str, enum.Enum):
    HORIZONTAL_POS = "Horizontal position",
    VERTICAL_POS = "Vertical position",
    ORIENTATION = "Orientation"


class COMMANDS(str, enum.Enum):
    REPORT = "REPORT",
    PLACE = "PLACE",
    MOVE = "MOVE",
    LEFT = "LEFT",
    RIGHT = "RIGHT"
