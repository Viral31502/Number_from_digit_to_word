from number_set_namer import NumberList
from data import group_name


def reverse(list_to_reverse):
    new_list = []
    for i in range(len(list_to_reverse)-1, -1, -1):
        new_list.append(list_to_reverse[i])
    return new_list


def shorter_list_maker(num):
    temp_list = []
    for i in range(3):
        ratio = num % 10
        temp_list.append(ratio)
        num = int(num/10)
    # print(temp_list)
    return reverse(temp_list)


class Number:
    def __init__(self, user_input):
        self.final_list_dic = {}
        self.number = user_input
        self.final_name = self.do_naming()
        self.final_list = []


    def do_naming(self):
        self.final_list = self.list_of_list()
        self.populate_dic()
        name = self.name_number()
        if name == "":
            name = "Zero"
        return name

    def list_of_list(self):
        temp_list = []
        while self.number > 0:
            three_digit = self.number % 1000
            # print(f"three digit {three_digit}")
            temp_list.append(shorter_list_maker(three_digit))

            self.number = int(self.number/1000)
            # print(f"long list {temp_list}")

        temp_list = reverse(temp_list)
        return temp_list

    def name_number(self):
        names = ""
        list_size = len(self.final_list_dic)
        for list_key in self.final_list_dic:
            list_to_name = NumberList(self.final_list_dic[list_key])
            temp_name = list_to_name.list_name
            position = list_key
            name_number = list_size - position - 1
            # print(f"group name {name_number}")
            # attributing the group names
            if temp_name != "":
                temp_name += group_name[name_number]
            if temp_name != "":
                if name_number == 0 and names != "" and "hundred" not in temp_name:
                    names = names + 'and ' + temp_name
                else:
                    names += temp_name
        return names

    def populate_dic(self):
        legnth_of_list = len(self.final_list)
        for i in range(0, legnth_of_list):
            self.final_list_dic[i] = self.final_list[i]


# because of repetition we need to find a new way to give group name because all groups with simlar names will
# automatically take the name of the highest group
