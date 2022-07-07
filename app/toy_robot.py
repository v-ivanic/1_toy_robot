import app.helpers as helpers
from app.enums import FACING, STATE_KEYS, COMMANDS


class ToyRobot(object):

    def __init__(self):
        self.state = dict.fromkeys([STATE_KEYS.HORIZONTAL_POS, STATE_KEYS.VERTICAL_POS, STATE_KEYS.ORIENTATION])

    def report(self):
        print("Reporting: " + str(self.state[STATE_KEYS.HORIZONTAL_POS]) + "," +
              str(self.state[STATE_KEYS.VERTICAL_POS]) + "," +
              str(self.state[STATE_KEYS.ORIENTATION]))

    def place(self, place_arg):
        """
        Update state for PLACE command with passed arguments.
        :param: place_arg: arguments for PLACE command e.g. '1,2,EAST'
        :return: state: updated state
        """
        # Check of place arguments is done earlier. Args can be used as is.
        x = int(place_arg.split(',')[0])
        y = int(place_arg.split(',')[1])
        f = place_arg.split(',')[2]
        self.state.update({STATE_KEYS.HORIZONTAL_POS: x, STATE_KEYS.VERTICAL_POS: y, STATE_KEYS.ORIENTATION: f})

    # Customer requirements:
    #   - Any movement that would result in the robot falling from the table must be prevented.
    #   - The toy robot must not fall off the table during movement.
    #   - Any move that would cause the robot to fall must be ignored.
    def _state_validation(self):
        """
        Used for state check before and after for MOVE, LEFT, RIGHT.
        Used for state check before LEFT and RIGHT.
        :return: True if horizontal check, vertical check and orientation check are satisfied
                 False if either of checks fails
        """
        hor_check = (-1 < int(self.state[STATE_KEYS.HORIZONTAL_POS]) < 5)
        ver_check = (-1 < int(self.state[STATE_KEYS.VERTICAL_POS]) < 5)
        ori_check = self.state[STATE_KEYS.ORIENTATION] in (FACING.NORTH, FACING.SOUTH, FACING.EAST, FACING.WEST)
        if hor_check and ver_check and ori_check:
            return True
        else:
            print("BOOM! You tried to MOVE a toy outside of table dimensions or it lost its orientation.")
            print("ACME corp. safety measures discarded wrong toy movement and prevented its destruction.")
            return False

    # Customer requirements:
    #   - MOVE will move the toy robot one unit forward in the direction it is currently facing.
    def move(self):
        is_state_valid_before_update = self._state_validation()

        if is_state_valid_before_update:
            state_backup = self.state.copy()

            # TODO: think of better way to handle this, not with if ... elif ...
            if self.state[STATE_KEYS.ORIENTATION] == FACING.NORTH:
                self.state.update({STATE_KEYS.VERTICAL_POS: (self.state[STATE_KEYS.VERTICAL_POS] + 1)})

            elif self.state[STATE_KEYS.ORIENTATION] == FACING.SOUTH:
                self.state.update({STATE_KEYS.VERTICAL_POS: (self.state[STATE_KEYS.VERTICAL_POS] - 1)})

            elif self.state[STATE_KEYS.ORIENTATION] == FACING.EAST:
                self.state.update({STATE_KEYS.HORIZONTAL_POS: (self.state[STATE_KEYS.HORIZONTAL_POS] + 1)})

            elif self.state[STATE_KEYS.ORIENTATION] == FACING.WEST:
                self.state.update({STATE_KEYS.HORIZONTAL_POS: (self.state[STATE_KEYS.HORIZONTAL_POS] - 1)})

            # Undo updated state if state is invalid.
            is_state_valid_after_update = self._state_validation()

            if not is_state_valid_after_update:
                self.state = state_backup.copy()

    # Customer requirements:
    #   - LEFT and RIGHT will rotate the robot 90 degrees in the specified direction
    #   without changing the position of the robot.
    def left(self):
        is_state_valid = self._state_validation()

        if is_state_valid:
            left_rotate = {
                FACING.NORTH: FACING.WEST,
                FACING.WEST: FACING.SOUTH,
                FACING.SOUTH: FACING.EAST,
                FACING.EAST: FACING.NORTH
            }
            self.state.update({STATE_KEYS.ORIENTATION: left_rotate[self.state[STATE_KEYS.ORIENTATION]]})

    def right(self):
        is_state_valid = self._state_validation()

        if is_state_valid:
            right_rotate = {
                FACING.NORTH: FACING.EAST,
                FACING.EAST: FACING.SOUTH,
                FACING.SOUTH: FACING.WEST,
                FACING.WEST: FACING.NORTH
            }
            self.state.update({STATE_KEYS.ORIENTATION: right_rotate[self.state[STATE_KEYS.ORIENTATION]]})

    def start_the_game(self):
        """
        Wrapper of main functionality, which only takes input from user and proceeds to main part
        Main functionality starts here. It reads raw input; checks and formats the input;
        runs commands for state update.
        :param: self:
        """
        print("The Little Toy Robot That Could doesn't know where it is and where to move :(")
        print("Checkout readme.md and help the robot to move :)")
        input_raw = input("Enter command:")
        match helpers.check_and_format_input(input_raw):
            case True, input_filtered:
                # input_filtered: checked and formatted array of strings representing commands only containing
                # REPORT, MOVE, LEFT, RIGHT, PLACE X,Y,F
                # Send each command separately.
                for command in input_filtered:
                    self._update_state(command)
                print("Looks like Little Toy Robot That Could survived your sequence of commands!")
            case False:
                print("Not a single valid PLACE command!")
            case _:
                raise Exception("ERROR: unexpected return")

    def _update_state(self, single_command):
        """
        Update state. There are 2 type of commands:
        1. doesn't update the state - REPORT
        2. updates the state - MOVE, LEFT, RIGHT, PLACE X,Y,F
            These commands are arranged in array and formatted for execution.
            They follow the same generic behaviour: execute command, which in turn changes the state.
        :param: single_command: single command from checked and formatted array of strings representing commands.
        Containing only REPORT, MOVE, LEFT, RIGHT, PLACE X,Y,F.
        """
        # split incoming command as it can be PLACE X,Y,F
        match single_command.split()[0]:
            # REPORT doesn't need to update the state
            # Customer requirements: REPORT will announce the X,Y and orientation of the robot.
            case COMMANDS.REPORT:
                self.report()
            # everything else (MOVE, LEFT, RIGHT, PLACE X,Y,F) updates the state
            case COMMANDS.PLACE:
                # send PLACE args for state update
                self.place(single_command.split()[1])
            case COMMANDS.MOVE:
                self.move()
            case COMMANDS.LEFT:
                self.left()
            case COMMANDS.RIGHT:
                self.right()
            # adding Exception in case check and formatting of input command went wrong.
            case _:
                raise Exception("Received unexpected command and exploded!")
