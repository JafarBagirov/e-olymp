Rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
Ar = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def Roman(arab):
    roman = ""
    i = 0
    while arab > 0:
        while Ar[i] <= arab:
            roman += Rom[i]
            arab -= Ar[i]
        i += 1
    return roman

def Arab(roman):
    arab = 0
    i = 0
    while roman:
        while roman.startswith(Rom[i]):
            roman = roman[len(Rom[i]):]
            arab += Ar[i]
        i += 1
    return arab

def main():
    input_str = input()

    first, second = input_str.split('+')

    toplam = Arab(first) + Arab(second)

    result = Roman(toplam)
    print(result)

if __name__ == "__main__":
    main()
