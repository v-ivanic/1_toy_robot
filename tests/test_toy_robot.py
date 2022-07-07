import pytest
from app.toy_robot import ToyRobot
from app.enums import FACING, STATE_KEYS


# Module level testing.
# Class ToyRobot is module which is tested.

# Customer example of inputs and outputs:
command_1 = "PLACE 0,0,NORTH MOVE REPORT"
result_1 = {STATE_KEYS.HORIZONTAL_POS: 0, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.NORTH}

command_2 = "PLACE 0,0,NORTH LEFT REPORT"
result_2 = {STATE_KEYS.HORIZONTAL_POS: 0, STATE_KEYS.VERTICAL_POS: 0, STATE_KEYS.ORIENTATION: FACING.WEST}

command_3 = "PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT"
result_3 = {STATE_KEYS.HORIZONTAL_POS: 3, STATE_KEYS.VERTICAL_POS: 3, STATE_KEYS.ORIENTATION: FACING.NORTH}

# Checking that state is not set after invalid PLACE command.
command_4 = "PLACE 7,7,NORTH MOVE"
result_4 = {STATE_KEYS.HORIZONTAL_POS: None, STATE_KEYS.VERTICAL_POS: None, STATE_KEYS.ORIENTATION: None}

# Long command that test multiple wrong placement,moving from the edge of board and place without arguments.
command_5 = "PLACE 7,7,NORTH MOVE PLACE 4,4,NORTH MOVE RIGHT PLACE LEFT PLACE 7,7,NORTH LEFT MOVE REPORT PLACE"
result_5 = {STATE_KEYS.HORIZONTAL_POS: 3, STATE_KEYS.VERTICAL_POS: 4, STATE_KEYS.ORIENTATION: FACING.WEST}

# Checking invalid place args.
command_6 = "PLACE 0,0 MOVE RIGHT"
result_6 = {STATE_KEYS.HORIZONTAL_POS: None, STATE_KEYS.VERTICAL_POS: None, STATE_KEYS.ORIENTATION: None}


@pytest.mark.parametrize("command,result", [(command_1, result_1), (command_2, result_2), (command_3, result_3),
                                            (command_4, result_4), (command_5, result_5), (command_6, result_6)])
def test_commands(command, result, monkeypatch):

    robot_toy = ToyRobot()
    monkeypatch.setattr('builtins.input', lambda _: command)
    robot_toy.start_the_game()
    assert robot_toy.state == result


# Method move as a part of module ToyRobot testing.
# Test that move will prevent failure from table.
state_1 = {STATE_KEYS.HORIZONTAL_POS: 4, STATE_KEYS.VERTICAL_POS: 4, STATE_KEYS.ORIENTATION: FACING.NORTH}
result_1 = {STATE_KEYS.HORIZONTAL_POS: 4, STATE_KEYS.VERTICAL_POS: 4, STATE_KEYS.ORIENTATION: FACING.NORTH}
state_2 = {STATE_KEYS.HORIZONTAL_POS: 4, STATE_KEYS.VERTICAL_POS: 4, STATE_KEYS.ORIENTATION: FACING.EAST}
result_2 = {STATE_KEYS.HORIZONTAL_POS: 4, STATE_KEYS.VERTICAL_POS: 4, STATE_KEYS.ORIENTATION: FACING.EAST}
state_3 = {STATE_KEYS.HORIZONTAL_POS: 0, STATE_KEYS.VERTICAL_POS: 0, STATE_KEYS.ORIENTATION: FACING.SOUTH}
result_3 = {STATE_KEYS.HORIZONTAL_POS: 0, STATE_KEYS.VERTICAL_POS: 0, STATE_KEYS.ORIENTATION: FACING.SOUTH}
state_4 = {STATE_KEYS.HORIZONTAL_POS: 0, STATE_KEYS.VERTICAL_POS: 0, STATE_KEYS.ORIENTATION: FACING.WEST}
result_4 = {STATE_KEYS.HORIZONTAL_POS: 0, STATE_KEYS.VERTICAL_POS: 0, STATE_KEYS.ORIENTATION: FACING.WEST}
# Test basic move functionality.
state_5 = {STATE_KEYS.HORIZONTAL_POS: 2, STATE_KEYS.VERTICAL_POS: 2, STATE_KEYS.ORIENTATION: FACING.NORTH}
result_5 = {STATE_KEYS.HORIZONTAL_POS: 2, STATE_KEYS.VERTICAL_POS: 3, STATE_KEYS.ORIENTATION: FACING.NORTH}
state_6 = {STATE_KEYS.HORIZONTAL_POS: 2, STATE_KEYS.VERTICAL_POS: 2, STATE_KEYS.ORIENTATION: FACING.SOUTH}
result_6 = {STATE_KEYS.HORIZONTAL_POS: 2, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.SOUTH}
state_7 = {STATE_KEYS.HORIZONTAL_POS: 2, STATE_KEYS.VERTICAL_POS: 2, STATE_KEYS.ORIENTATION: FACING.EAST}
result_7 = {STATE_KEYS.HORIZONTAL_POS: 3, STATE_KEYS.VERTICAL_POS: 2, STATE_KEYS.ORIENTATION: FACING.EAST}
state_8 = {STATE_KEYS.HORIZONTAL_POS: 2, STATE_KEYS.VERTICAL_POS: 2, STATE_KEYS.ORIENTATION: FACING.WEST}
result_8 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 2, STATE_KEYS.ORIENTATION: FACING.WEST}


@pytest.mark.parametrize("state,result", [(state_1, result_1), (state_2, result_2),
                                          (state_3, result_3), (state_4, result_4),
                                          (state_5, result_5), (state_6, result_6),
                                          (state_7, result_7), (state_8, result_8)])
def test_move(state, result):
    robot_toy = ToyRobot()
    robot_toy.state = state.copy()
    robot_toy.move()
    assert robot_toy.state == result


# Method left as a part of module ToyRobot testing.
state_1 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.SOUTH}
result_1 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.EAST}
state_2 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.EAST}
result_2 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.NORTH}
state_3 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.NORTH}
result_3 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.WEST}
state_4 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.WEST}
result_4 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.SOUTH}


@pytest.mark.parametrize("state,result", [(state_1, result_1), (state_2, result_2),
                                          (state_3, result_3), (state_4, result_4)])
def test_left(state, result):
    robot_toy = ToyRobot()
    robot_toy.state = state.copy()
    robot_toy.left()
    assert robot_toy.state == result


# Method right as a part of module ToyRobot testing.
state_0 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.EAST}
result_0 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.SOUTH}
state_1 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.SOUTH}
result_1 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.WEST}
state_2 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.WEST}
result_2 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.NORTH}
state_3 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.NORTH}
result_3 = {STATE_KEYS.HORIZONTAL_POS: 1, STATE_KEYS.VERTICAL_POS: 1, STATE_KEYS.ORIENTATION: FACING.EAST}


@pytest.mark.parametrize("state,result", [(state_0, result_0), (state_1, result_1), (state_2, result_2),
                                          (state_3, result_3)])
def test_right(state, result):
    robot_toy = ToyRobot()
    robot_toy.state = state.copy()
    robot_toy.right()
    assert robot_toy.state == result


pytest.main(["test_toy_robot.py", "-v"])
