def numbers_into_words(number):
    digits = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
        16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
        30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
    }
    thousand = 1000
    million = thousand * 1000
    billion = million * 1000
    trillion = billion * 1000

    final_number = []
    if number == 0:
        print(digits[number])
    elif number < 20:
        print(digits[number])
    elif number < 100 and number % 10 == 0:
        print(digits[number])
    elif number < 100 and number > 20 and number % 10 != 0:
        single = number % 10
        print(digits[number - single] + " " + digits[single])
    # elif number >= 100 and number % 100 == 0:
    #   print(digits[number // 100] + ' Hundred')
    # elif number >= 100 and number % 100 != 0:
    #   print(digits[number // 100] + ' Hundred ' + digits[number % 10])

