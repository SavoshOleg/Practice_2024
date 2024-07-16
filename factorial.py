def factorial(n):
    """Обчислює факторіал числа n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    number = int(input("Введіть число для обчислення факторіалу: "))
    result = factorial(number)
    print(f"Факторіал числа {number} дорівнює {result}.")
