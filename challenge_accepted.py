"""
Challenge Accepted

By : Jakgri Klabdi (https://github.com/tongJK)

UUsing : Python 3.6.6

Started : 30/9/2020 20.50

Finished : 10/11/2020 21.10
"""

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


if __name__ == '__main__':

    while True:
        int_result = None
        given_input = input('Enter your input: ')

        for alphabet in given_input:
            if alphabet in digits:
                if int_result:
                    int_result = (int_result*10) + digits[alphabet]
                else:
                    int_result = digits[alphabet]

        print('given input is "{}", result is {}\n'.format(given_input, int_result))
