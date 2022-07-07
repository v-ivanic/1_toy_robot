from app.enums import FACING, COMMANDS


# Helper functions that are not using ToyRobot state attribute

# Customer requirements:
#   - The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued,
#     in any order, including another PLACE command.
#   - The application should discard all commands in the sequence until a valid PLACE command has been executed.
#   - A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.
#   - Square tabletop, of dimensions 5 units x 5 units
#   - Robot ... must be prevented from falling to destruction.
#   - The toy robot must not fall off ... includes the initial placement of the toy robot.
#   - The application should discard all commands in the sequence until a valid PLACE command has been executed.
def check_and_format_input(input_raw):
    """
    Checks and formats input string into array of commands for toy robot
    :param: input_raw(string): string input from user
    :return:
        True(bool), input_filtered[array(string)]: checks and formatting is OK
        False(bool): checks and/or formatting is NOT OK
    """
    input_split = input_raw.split()
    # create empty array input_filtered which will be filled with OK commands
    input_filtered = []
    # bool at_least_one_place_ok used to discard everything before valid PLACE
    at_least_one_place_ok = False

    # TODO: for .. if ... elif ... if. To much nesting, reduce complexity.
    for count, command in enumerate(input_split):

        # check if PLACE exists
        place_exists = (command == COMMANDS.PLACE)
        # check if last PLACE args exits
        place_arg_exits = (len(input_split) > (count+1))
        # check if place args are OK
        try:
            place_args_ok = check_place_arg(input_split[count + 1])
        except IndexError:
            place_args_ok = False

        if place_exists and place_arg_exits and place_args_ok:
            at_least_one_place_ok = True
            # concatenate PLACE and X,Y,F into one string
            input_filtered.append(str(command) + " " + input_split[count + 1])

        # check if other elements are MOVE, LEFT, RIGHT, REPORT
        elif command in (COMMANDS.MOVE, COMMANDS.LEFT, COMMANDS.RIGHT, COMMANDS.REPORT):
            # discard everything before valid PLACE command
            if at_least_one_place_ok:
                input_filtered.append(command)

        # discard everything that is not PLACE, MOVE, LEFT, RIGHT, REPORT

    if at_least_one_place_ok:
        return True, input_filtered
    else:
        return False


def check_place_arg(arg):
    """
    Checks place arguments for right type and formatting: X,Y,F
    :param: arg(string): string input for place
    :return:
        True(bool): arguments are in right format: X,Y,F
        False(bool): arguments are NOT OK
    """
    arg_split = arg.split(',')
    # toy life-saving check
    # TODO: 6 conditions inside if. Move to separate functions or variables as in check_and_format_input
    if len(arg_split) == 3 and \
            str.isnumeric(arg_split[0]) and -1 < int(arg_split[0]) < 5 and\
            str.isnumeric(arg_split[1]) and -1 < int(arg_split[1]) < 5 and\
            arg_split[2] in (FACING.NORTH, FACING.WEST, FACING.EAST, FACING.SOUTH):
        return True
    else:
        return False
