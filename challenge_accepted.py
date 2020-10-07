"""
Challenge Accepted.

By : Jakgri Klabdi (https://github.com/tongJK)

UUsing : Python 3.6.6

Started : 30/9/2020 20.50

Finished : 30/9/2020 21.10

Edited : 07/10/2020 19.25
"""


digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def string2int(sentence_input):
    """
    This is my function to extract numerical from any input sentence
    """
    result = None
    for alphabet in sentence_input:
        if alphabet in digits:
            if result:
                result = (result*10) + digits[alphabet]
            else:
                result = digits[alphabet]

    return result


if __name__ == '__main__':

    # #
    # # ---------- use this block for set value's input ------------------------------------------------------------
    #
    # test_list = ['abc573', 'a5b7c3', 'fsipfjqw0-efjqw0-mpefmpหดาย-/ตคภ/ตค/--++ ', 'asdasd', '123456789']
    #
    # for i, test in enumerate(test_list):
    #     int_result = string2int(test)
    #     print('test {} : input is "{}", my funtion\'s result is "{}", type of result is {}'.format(
    #         (i+1), test, int_result, type(int_result)))
    # # ------------------------------------------------------------------------------------------------------------

    #
    # ---------- use this block for set keyboard's input ---------------------------------------------------------

    while True:
        given_input = input('Enter your input: ')
        int_result = string2int(given_input)
        print('given input is "{}", result is {}, type of result is {}\n'.format(
            given_input, int_result, type(int_result)))

    # ------------------------------------------------------------------------------------------------------------
