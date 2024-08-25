import datetime
import json
import os

date_today = datetime.datetime.now()
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "area-full.json"), encoding="utf-8") as f:
    regions = json.load(f)


class id_card_verification(object):
    def __init__(self, id: str):
        """
        initialization and call functions.
        """

        self.id_number = id
        self.id_number_list = list(id)


    def check_length(self) -> bool:
        """
        check the length of an id number.

        Returns:
            bool: if the number meets the conditions
        """

        if len(self.id_number_list) == 18:
            if self.id_number_list[17] == "X":
                self.id_number_list[17] = "10"
            return True
        else:   
            return False


    def check_city_code(self) -> str:
        """check the city code of an id number.

        Returns:
            str: city name (provinces + city + district)
        """

        name_level_provinces = name_level_city = name_level_district = "?"

        for provinces in regions:
            if provinces["adcode"][0:2] == self.id_number[0:2]:
                name_level_provinces = provinces["name"]
                break

        if name_level_provinces != "?":
            for city in provinces["districts"]:
                if city["adcode"][2:4] == self.id_number[2:4]:
                    name_level_city = city["name"]
                    break

        if name_level_city != "?":
            for districts in city["districts"]:
                if districts["adcode"][4:6] == self.id_number[4:6]:
                    name_level_district = districts["name"]
                    break

        return name_level_provinces+name_level_city+name_level_district


    def check_verification_number(self) -> bool:
        """check if the verification number is correct.

        Returns:
            bool: if the number meets the conditions
        """        
        
        times = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        verification_number = (1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2)
        total = 0
        try:
            for i in range(0, 17):
                total += int(self.id_number_list[i]) * times[i]
            
            checking = total % 11
            checking = verification_number[checking]

            if int(self.id_number_list[17]) == checking:
                return True
            else:   
                return False

        except ValueError:
            return False


    def check_age(self) -> tuple:
        """
        check the person is an adult or a children according to the id number.

        Returns:
            tuple[str, int]: the person is an adult or a children and his/her age
        """

        date_birth = datetime.date(int(self.id_number[6:10]), int(self.id_number[10:12]), int(self.id_number[12:14]))
        age = date_today.year - date_birth.year - ((date_today.month, date_today.day) < (date_birth.month, date_today.day))
        
        if age >= 18:
            return "成年人", age
        elif age < 0:
            raise ValueError
        else:
            return "青少年", age
