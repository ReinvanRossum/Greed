class Greed():
    @staticmethod
    def score(dice_list=[]):
        score = 0
        Greed.check_number_of_dice(dice_list)

        if dice_list.count(5) < 3:
            score += 50 * dice_list.count(5)
        if dice_list.count(1) < 3:
            score += 100 * dice_list.count(1)
        score = Greed.find_straight(dice_list, score)
        score = Greed.find_three_pairs(dice_list, score)
        score = Greed.find_more_of_a_kind(dice_list, score)

        return score

    @staticmethod
    def check_number_of_dice(dice_list):
        if len(dice_list) > 6:
            raise AssertionError

    @staticmethod
    def find_more_of_a_kind(dice_list, score):
        for counted_die in range(3, 7):
            if dice_list.count(1) == counted_die:
                score += 1000 * 2**(counted_die - 3)
        for die in range(2, 7):
            for counted_die in range(3, 7):
                if dice_list.count(die) == counted_die:
                    score += die * 100 * 2**(counted_die - 3)
        return score

    @staticmethod
    def find_three_pairs(dice_list, score):
        pairs = [
            dice_list.count(2) == 2,
            dice_list.count(3) == 2,
            dice_list.count(4) == 2,
            dice_list.count(5) == 2,
            dice_list.count(6) == 2
        ]
        if sum(pairs) == 3:
            score = 800
        return score

    def find_straight(dice_list, score):
        if set(dice_list) == set([1, 2, 3, 4, 5, 6]):
            score = 1200
        return score
