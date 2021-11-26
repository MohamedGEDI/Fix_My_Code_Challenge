# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            tmp_result.append("FizzBuzz")
        elif i % 3 == 0:
            tmp_result.append("Fizz")
        elif i % 5 == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    fizzbuzz(50)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
