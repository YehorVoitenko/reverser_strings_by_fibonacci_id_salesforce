import logging

from manager.static import FILE_PATH, TYPE_ERROR, VALUE_ERROR, ERROR


class Manager:
    @staticmethod
    def calculate_perfect_square(number: int):
        seq = int(number**0.5)
        return seq * seq == number

    @staticmethod
    def check_value_for_fibonacci_belonging(number: int) -> int:
        constant_calculation = number**2 * 5
        return Manager.calculate_perfect_square(constant_calculation + 4) \
               or Manager.calculate_perfect_square(constant_calculation - 4)

    @staticmethod
    def get_result_by_txt_file(array):
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
                            f'reverse value: {Manager.check_value_for_fibonacci_belonging(i)} | '
                            f'len array: {len(array)}')
            if Manager.check_value_for_fibonacci_belonging(i):
                result_array.append(array[i-1][::-1])
            else:
                result_array.append(array[i-1])
            Manager.get_result_by_txt_file(result_array)

        return result_array
