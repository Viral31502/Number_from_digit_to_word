from data import values, tens_values, next_values


def hun_evaluate(val):
    if val != 0:
        return values[val] + "hundred "
    else:
        return ""


class NumberList:
    def __init__(self, lists):
        self.num_list = lists
        self.hundred = ""
        self.tens = ""
        self.unit = ""
        self.list_name = self.name_number_group_of_3()

    def name_number_group_of_3(self):
        for i in range(0, 3):
            if i == 0:
                self.hundred = hun_evaluate(self.num_list[i])
            elif i == 1:
                self.tens = self.tens_evaluate(self.num_list[i])
        if self.hundred == "":
            return self.tens
        else:
            if self.tens != "":
                return self.hundred + "and" + " " + self.tens
            else:
                return self.hundred

    def tens_evaluate(self, val):
        if val == 1:
            return next_values[self.num_list[2]]
        elif val > 1:
            return tens_values[val]  + values[self.num_list[2]]
        elif val == 0:
            return values[self.num_list[2]]
