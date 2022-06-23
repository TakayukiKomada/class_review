import math
from decimal import Decimal, ROUND_HALF_UP


class Rectangle:
    def __init__(
        self,
        height,
        width,
    ):
        self.height = height
        self.width = width

    def area(self):
        ans = round(self.height * self.width)
        ans2 = Decimal(ans).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return ans2

    def diagonal(self):
        answer = math.sqrt((self.height**2 + self.width**2))
        return round(answer, 2)


if __name__ == "__main__":

    rectangle1 = Rectangle(height=5, width=6)
    print(rectangle1.area())  # 30.00
    print(rectangle1.diagonal())  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    print(rectangle2.area())  # 9.00
    print(rectangle2.diagonal())  # 4.24
