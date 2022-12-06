input_file = open("Day2/input", "r")
lines = [line.rstrip() for line in input_file]
input_file.close()


def get_outcome_original(play, response):
    """
    plays
    A - Rock
    B - Paper
    C - Scissors

    responses
    X - Rock
    Y - Paper
    Z - Scissors

    Scores:
    1 - X rock
    2 - Y paper
    3 - Z Scissors
    plus score for outcome:
    - 0 lost
    - 3 draw
    - 6 win
    """

    # result
    scores_map = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }
    response_points = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    return scores_map[play][response] + response_points[response]


def get_outcome_new_rules(play, outcome):
    """
    plays
    A - Rock
    B - Paper
    C - Scissors

    responses
    X - lose
    Y - draw
    Z - win

    Scores:
    1 - X rock
    2 - Y paper
    3 - Z Scissors
    plus score for outcome:
    - 0 lost
    - 3 draw
    - 6 win
    """
    # result
    response = {
        # Rock
        "A": {"X": "scissors", "Y": "rock", "Z": "paper"},
        # Paper
        "B": {"X": "rock", "Y": "paper", "Z": "scissors"},
        # Scissors
        "C": {"X": "paper", "Y": "scissors", "Z": "rock"},
    }
    outcome_points = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    shape_point = {"rock": 1, "paper": 2, "scissors": 3}

    return shape_point[response[play][outcome]] + outcome_points[outcome]


def get_score(get_outcome):
    score = 0
    for game_round in lines:
        play, response = game_round.split(" ")
        score = score + get_outcome(play, response)
    return score


def day2():
    print("Original rules score: {}".format(get_score(get_outcome_original)))
    print("Updated rules score: {}".format(get_score(get_outcome_new_rules)))
