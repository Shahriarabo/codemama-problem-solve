def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
if __name__ == "__main__":
    celsius = float(input())
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("The temperature in Fahrenheit is: {:.2f}".format(fahrenheit))
