class Greed():

    @staticmethod
    def score(dice_list=[]):
        Greed.check_number_of_dice(dice_list)
        if dice_list.count(5) == 1:
            return 50
        for counted_die in range(3, 7):
            if dice_list.count(1) == counted_die:
                return 1000 * 2**(counted_die - 3)
        for die in range(2, 7):
            for counted_die in range(3, 7):
                if dice_list.count(die) == counted_die:
                    return die * 100 * 2**(counted_die - 3)
        return 100

    @staticmethod
    def check_number_of_dice(dice_list):
        if len(dice_list) > 6:
            raise AssertionError
