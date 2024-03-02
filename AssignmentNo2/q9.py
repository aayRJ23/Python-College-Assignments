def evaluate_series(m, n):
    total = 0
    for i in range(1, n + 1):
        total += i ** m
    return total

def main():
    m = int(input("Enter the value of m: "))
    n = int(input("Enter the value of n: "))

    result = evaluate_series(m, n)
    print(f"The result of the series 1^{m} + 2^{m} + 3^{m} + ... + {n}^{m} is: {result}")

if __name__ == "__main__":
    main()
