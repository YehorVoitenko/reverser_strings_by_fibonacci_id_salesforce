import logging

from manager.static import FILE_PATH, TYPE_ERROR, VALUE_ERROR, ERROR


class Manager:
    @staticmethod
    def check_number_for_fibonacci_sequence(number: int) -> bool:
        if number == 0 or number == 1:
            return True

        a, result = 0, 1
        while result < number:
            b = a + result
            a, result = result, b
        if result == number:
            return True
        else:
            return False

    @staticmethod
    def get_reversed_string(string: str) -> str:
        string_by_symbols = list(string)
        for index in range(len(string) // 2):
            current_letter_storage = string_by_symbols[index]

            # start letter replaced to last letter
            string_by_symbols[index] = string_by_symbols[len(string) - index - 1]

            # reverse replacing - last letter replaced to start letter
            string_by_symbols[len(string) - index - 1] = current_letter_storage
        return ''.join(string_by_symbols)

    @staticmethod
    def get_result_by_txt_file(array: list):
        logging.warning(f"Path for file storage: {FILE_PATH} in 'get_result_by_txt_file' method")
        with open(FILE_PATH, "w") as file:
            for i in array:
                file.write(i + '\n')

    @staticmethod
    def reverse_line_by_fibonacci_id(array: list) -> list:
        if not isinstance(array, list):
            logging.warning(f'ERROR {TYPE_ERROR} {type(array)}')
            return {f"{ERROR}": f'{TYPE_ERROR} {type(array)}'}

        elif len(array) == 0:
            logging.warning(f'ERROR {VALUE_ERROR} {len(array)}')
            return {f"{ERROR}": f'{VALUE_ERROR} {len(array)}'}

        result_array = []

        for i in range(1, len(array) + 1):
            logging.warning(f'Id number: {i} | '
                            f'value: {array[i-1]} | '
                            f'len array: {len(array)}')

            if not isinstance(array[i - 1], str):
                return {f"{ERROR}": f'Value should be string, not {type(array[i - 1])}'}

            if Manager.check_number_for_fibonacci_sequence(i):
                result_array.append(Manager.get_reversed_string(array[i-1]))
            else:
                result_array.append(array[i-1])
            Manager.get_result_by_txt_file(result_array)

        return result_array
