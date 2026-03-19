from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.validation = False
        self.output = ""
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return f"{data}"
            else:
                sum = 0
                processed = 0
                for num in data:
                    sum += num
                    processed += 1
                avg = sum / processed
                self.output = f"Output: Processed {processed} numeric values, sum={sum}, avg={avg}"
        finally:
            return f"{data}"

    def validate(self, data: list) -> bool:
        try:
            if not isinstance(data, list):
                raise ValueError()
            for num in data:
                if not isinstance(num, int):
                    raise TypeError()
        except ValueError:
            self.output = "Output: ERROR, data is not a list"
            return False
        except TypeError:
            self.output = "Output: ERROR, Non-numeric data detected"
            return False
        else:
            return True
        finally:
            self.validation = True

    def format_output(self, result: str) -> str:
        try:
            if not result:
                raise ValueError()
        except ValueError:
            if not self.validation:
                print("Validation: Numeric data doesn't verified")
        finally:
            print("Validation: Numeric data verified")
            return self.output


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.output = ""
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError()
            else:
                lenght = len(data)
                word_count = len(data.split(data, " "))
                self.output = f"Output: Processed text: {lenght} characters, {word_count} words"
        finally:
            return f'"{data}"'

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                raise ValueError()
        except ValueError:
            self.output = "Output: Invalid text"
            return False
        else:
            return True

    def format_output(self, result: str) -> str:
        print("Validation: Text data verified")
        return self.output



class LogProcessor(DataProcessor):
    pass


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_processor = NumericProcessor()
    lst = [1, 2, 3, 4, 5]
    result = num_processor.process(lst)
    print("Processing data:", result)
    print(num_processor.format_output(result))
    print()

    txt_processor = TextProcessor()
    result = txt_processor.process("Hello Nexus World")
    print("Processing data:", result)
    print(txt_processor.format_output(result))
    print()
