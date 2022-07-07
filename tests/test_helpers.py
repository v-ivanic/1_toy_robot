import pytest
import app.helpers as helpers

# Unit level testing

input_raw_0 = "PLACE 0,0,NORTH MOVE REPORT"
result_0 = ['PLACE 0,0,NORTH', 'MOVE', 'REPORT']

input_raw_1 = "PLACE 0,0,NORTH LEFT REPORT"
result_1 = ['PLACE 0,0,NORTH', 'LEFT', 'REPORT']

input_raw_2 = "PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT"
result_2 = ['PLACE 1,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'REPORT']

# Checking that state is not set after invalid PLACE command.
# input_raw_3 = "PLACE 7,7,NORTH MOVE"
# result_3 = {'Horizontal position': None, 'Vertical position': None, 'Orientation': None}

# Long command that test multiple wrong placement,moving from the edge of board and place without arguments.
input_raw_4 = "PLACE 7,7,NORTH MOVE PLACE 4,4,NORTH MOVE RIGHT PLACE LEFT PLACE 7,7,NORTH LEFT MOVE REPORT PLACE"
result_4 = ['PLACE 4,4,NORTH', 'MOVE', 'RIGHT', 'LEFT', 'LEFT', 'MOVE', 'REPORT']

# Checking invalid place args.
# input_raw_5 = "PLACE 0,0 MOVE RIGHT"
# result_5 = {'Horizontal position': None, 'Vertical position': None, 'Orientation': None}

# TODO: ADD CHECKING OF TRUE/FALSE AND COMMENTED CASES FROM ABOVE


@pytest.mark.parametrize("input_raw,result", [(input_raw_0, result_0), (input_raw_1, result_1),
                                            (input_raw_2, result_2), (input_raw_4, result_4)])
def test_commands(input_raw, result):
    _, tmp = helpers.check_and_format_input(input_raw)
    assert tmp == result


# TODO: unit test check_place_arg.


pytest.main(["test_helpers.py", "-v"])