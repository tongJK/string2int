"""
Challenge Accepted

By : Jakgri Klabdi (https://github.com/tongJK)

UUsing : Python 3.6.6

Started : 30/9/2020 20.50

Finished : 30/9/2020 21.10
"""


digits = '0123456789'


def string2int(sentence_input):
    """
    This is my function to extract numerical from any input sentence
    """
    result = ''
    for alphabet in sentence_input:
        for digit in digits:
            if alphabet in digit:
                result = result + alphabet

    return int(result) if result else None


def recheck(sentence_input):
    """
    This function to recheck that my function(string2int) work well
    """

    return ''.join(filter(lambda i: i.isdigit(), sentence_input)) 


if __name__ == '__main__':

    #
    # ---------- use this block for set value's input ------------------------------------------------------------
    
    # test_list = ['abc573', 'a5b7c3', 'fsipfjqw0-efjqw0-mpefmpหดาย-/ตคภ/ตค/--++ ', 'asdasd', '123456789']
    # 
    # for i, test in enumerate(test_list):
    #     print('test {} : input is "{}", my funtion\'s result is {} and recheck result is {}'
    #           .format((i+1), test, string2int(test), recheck(test)))
    # ------------------------------------------------------------------------------------------------------------
    
    #
    # ---------- use this block for set keyboard's input ---------------------------------------------------------
    while True:
        given_input = input('Enter your input: ')
        int_result = string2int(given_input)
        print('given input is "{}", result is {}, type of result is {}\n'.format(
            given_input, int_result, type(int_result)))

    # ------------------------------------------------------------------------------------------------------------
