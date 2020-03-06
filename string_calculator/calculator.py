class Calculator:

    def add(self, string):
        self.string = string
        string_numbers = self.split_string(self.string)

        numbers = []
        negative_numbers = []
        for each in string_numbers:
            try:
                number = int(each)
            except:
                number = 0

            if number < 0:
                negative_numbers.append(number)
            numbers.append(number)

        if negative_numbers:
            message = ','.join([str(number) for number in negative_numbers])
            raise NegativesNotAllowedError(message)
        return sum(numbers)

    def split_string(self, string):
        self.string = string
        delimiter = ','
        if self.string.startswith('//'):
            delimiter = self.string[2]

            self.string = self.string[3:]

        self.string = self.string.replace('\n', delimiter)
        string_numbers = self.string.split(delimiter)
        return string_numbers


def NegativesNotAllowedError(Exception):
    pass


if __name__ == "__main__":
    string_calc = Calculator()

    addition = string_calc.add("2,5")
    print(addition)
