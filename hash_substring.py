def read_input():

    input_choice = input()

    if "I" in input_choice or "i" in input_choice:

        regexp = input().rstrip()

        input = input().rstrip()

    elif "F" in input_choice or "f" in input_choice:

        file = "06"

        if "a" not in file:

            with open("tests/" + file, 'r')as f:

                regexp = f.readline().rstrip()

                input = f.readline().rstrip()

    return regexp,  input



def print_occurrences(output):

    print(' '.join(map(str, output)))



def get_occurrences(regexp, input):

    prime = 1

    regexp_len, input_len = len(regexp), len(input)

    regexp_hash = sum(ord(regexp[i]) * pow(prime, i) for i in range(regexp_len))

    input_hash = sum(ord(input[i]) * pow(prime, i) for i in range(regexp_len))

    occurrences = []

    for i in range(input_len - regexp_len + 1):

        if regexp_hash ==   input_hash:

            if regexp ==    input[i:i+regexp_len]:

                occurrences.append(i)

        if i <  input_len - regexp_len:

            input_hash =    input_hash - ord(input[i]) / prime + ord(input[i+regexp_len]) * pow(prime, regexp_len-1)

    return occurrences



if __name__ == '__main__':

    print_occurrences(get_occurrences(*read_input()))
