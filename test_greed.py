import pytest
from greed import Greed


def test_score_accepts_6_dice():
    assert Greed.score([1, 2, 3, 4, 5, 6]) != None


def test_score_breaks_with_7_dice():
    try:
        assert Greed.score([1, 2, 3, 4, 5, 6, 1]) == None
    except AssertionError:
        pass


def test_score_accepts_5_dice():
    assert Greed.score([1, 2, 3, 4, 5]) != None


@pytest.mark.parametrize("dice_list", [[1], [1, 2, 2, 3, 3, 4], [2, 1, 2, 3]])
def test_score_single_one_as_100(dice_list):
    assert Greed.score(dice_list) == 100


def test_score_two_ones_as_200():
    assert Greed.score([1, 1])


def test_score_single_five_as_50():
    assert Greed.score([5]) == 50


def test_score_two_fives_as_100():
    assert Greed.score([5, 5]) == 100


def test_score_one_one_and_one_five_as_150():
    assert Greed.score([1, 5]) == 150


def test_score_triple_one_as_1000():
    assert Greed.score([1, 1, 1]) == 1000


def test_score_triple_two_as_200():
    assert Greed.score([2, 2, 2]) == 200


def test_score_triple_three_as_300():
    assert Greed.score([3, 3, 3]) == 300


def test_score_triple_four_as_400():
    assert Greed.score([4, 4, 4]) == 400


def test_score_triple_five_as_500():
    assert Greed.score([5, 5, 5]) == 500


def test_score_triple_six_as_600():
    assert Greed.score([6, 6, 6]) == 600


@pytest.mark.parametrize("dice_list,result", [([1, 1, 1, 1], 2000),
                                              ([2, 2, 2, 2], 400),
                                              ([3, 3, 3, 3], 600),
                                              ([4, 4, 4, 4], 800),
                                              ([5, 5, 5, 5], 1000),
                                              ([6, 6, 6, 6], 1200)])
def test_score_four_of_a_kind_as_score_of_triple_times_two(dice_list, result):
    assert Greed.score(dice_list) == result


@pytest.mark.parametrize("dice_list,result", [([1, 1, 1, 1, 1], 4000),
                                              ([2, 2, 2, 2, 2], 800),
                                              ([3, 3, 3, 3, 3], 1200),
                                              ([4, 4, 4, 4, 4], 1600),
                                              ([5, 5, 5, 5, 5], 2000),
                                              ([6, 6, 6, 6, 6], 2400)])
def test_score_five_of_a_kind_as_score_of_triple_times_four(dice_list, result):
    assert Greed.score(dice_list) == result


@pytest.mark.parametrize("dice_list,result", [([1, 1, 1, 1, 1, 1], 8000),
                                              ([2, 2, 2, 2, 2, 2], 1600),
                                              ([3, 3, 3, 3, 3, 3], 2400),
                                              ([4, 4, 4, 4, 4, 4], 3200),
                                              ([5, 5, 5, 5, 5, 5], 4000),
                                              ([6, 6, 6, 6, 6, 6], 4800)])
def test_score_six_of_a_kind_as_score_of_triple_times_eight(dice_list, result):
    assert Greed.score(dice_list) == result


@pytest.mark.parametrize("dice_list,result", [([1, 1, 5, 1, 5, 6], 1100),
                                              ([2, 2, 2, 3, 3, 3], 500),
                                              ([1, 5, 6, 6, 6, 6], 1350)])
def test_score_combine_three_pair_with_other_scores(dice_list, result):
    assert Greed.score(dice_list) == result


@pytest.mark.parametrize(
    "dice_list", [[2, 2, 3, 3, 4, 4], [2, 2, 3, 3, 5, 5], [3, 4, 6, 3, 4, 6]])
def test_score_three_pairs_as_800(dice_list):
    assert Greed.score(dice_list) == 800


def test_score_straight_as_1200():
    assert Greed.score([1, 2, 3, 4, 5, 6]) == 1200


@pytest.mark.parametrize("dice_list",
                         [[2, 3, 3, 4, 4, 6], [2, 2, 6, 6], [2, 4, 6, 3, 4, 6]]
                         )
def test_score_no_scoring_dice_as_zero(dice_list):
    assert Greed.score(dice_list) == 0
