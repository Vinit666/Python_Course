# modules
def circle(radius: float) -> None:
    area = 3.14 * radius * radius
    print(f"area of circle with {radius} radius : {area}")


def triangle(base: float, height: float) -> None:
    area = 0.5 * base * height
    print(f"area of triangle is  : {area}")


def rectangle(breadth: float, length: float) -> None:
    area = 3.14 * length * breadth
    print(f"area of rectangle is  : {area}")


if (
    __name__ == "__main__"
):  # this is use for only this python file not another import file
    circle(4.3)
    triangle(3.2, 1.4)
    rectangle(10.0, 5.5)
