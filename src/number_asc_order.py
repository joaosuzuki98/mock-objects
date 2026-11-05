from src.custom_stack_class import CustomStack


class NumberAscOrder:
    def sort(self, stack: CustomStack) -> list[int]:
        if not isinstance(stack, CustomStack):
            raise TypeError("stack deve ser uma instância de CustomStack")

        numbers = stack.elements.copy()
        if not numbers:
            return []

        if len(numbers) != 6:
            raise ValueError("a aposta deve conter exatamente seis números")

        if any(type(number) is not int for number in numbers):
            raise TypeError("os números da aposta devem ser inteiros")

        if any(number < 1 or number > 60 for number in numbers):
            raise ValueError("os números da aposta devem estar entre 1 e 60")

        if len(set(numbers)) != len(numbers):
            raise ValueError("os números da aposta não podem se repetir")

        return sorted(numbers)
