alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
illegal_first_letters = "ąęńóxy"
correct_word_with_one_letter = "aiouwz"
cyphertext = "kwędńłlśóxuqoriidyoużmźgacękukiźqąałrqiqćęwxzcmmbcipźvpnnqsłnbzęsbdrqśkłwśtogumixfńcpju"
cyphertext_oryginal = "kwędńłlśóxu_qo_riidy_o_użmźgacękukiź_qąałrqiqćę_w_xzcmmb_cipźvpnnqsłnb_zęsbd_rqśkłwśtogum_ixfńcpju"
words_with_2_letters = []
words_with_6_letters = []


def get_letter_by_number(cyphertext_numbers, position, number):
    index = (cyphertext_numbers[position] - number + len(alphabet)) % len(alphabet)
    return alphabet[index]

def create_numbers(text):
    text_numbers = []
    for i in range(len(text)):
        text_numbers.append(alphabet.index(text[i]))
    return text_numbers

def create_whole_key(key):
    whole_key = key + key
    while len(whole_key) < len(cyphertext):
        whole_key = key + whole_key
    return whole_key[0:len(cyphertext)]

def decrypt(cyphertext, key):
    cyphertext_numbers = create_numbers(cyphertext)

    whole_key = create_whole_key(key)
    whole_key_numbers = create_numbers(whole_key)
    result = []
    for i in range(len(cyphertext)):
        result.append(get_letter_by_number(cyphertext_numbers, i, whole_key_numbers[i]))
    result = "".join(result)
    if result[0] in illegal_first_letters:
        return False
    if result[18] not in correct_word_with_one_letter:
        return False
    if result[42] not in correct_word_with_one_letter:
        return False
    if result[11:13] not in words_with_2_letters:
        return False
    return result

def main():

    with open("dwuliterowe.txt", "r") as file:
        for line in file:
            words_with_2_letters.append(line.strip())
    with open("polskie_slowa_6_znakow.txt", "r") as f:
        for line in f:
            words_with_6_letters.extend(line.replace(',',' ').replace('.',' ').split())

    ct_6_letter_word = "xzcmmb"
    ct_numerical = [alphabet.index(c) for c in ct_6_letter_word]
    with open("1_2.txt", "a") as myfile:
        for word in words_with_6_letters:
            k1_candidates = []
            k2_candidates = []
            k3_candidates = []
            k4_candidates = []
            k5_candidates = []
            k6_candidates = []
            for i in range(6):
                for j in range(35):
                    if (alphabet.index(word[i]) + j) % 35 == ct_numerical[i]:
                        if i == 5:
                            k1_candidates.append(alphabet[j])
                        elif i == 0:
                            k2_candidates.append(alphabet[j])
                        elif i == 1:
                            k3_candidates.append(alphabet[j])
                        elif i == 2:
                            k4_candidates.append(alphabet[j])
                        elif i == 3:
                            k5_candidates.append(alphabet[j])
                        elif i == 4:
                            k6_candidates.append(alphabet[j])
            for k1 in k1_candidates:
                for k2 in k2_candidates:
                    for k3 in k3_candidates:
                        for k4 in k4_candidates:
                            for k5 in k5_candidates:
                                for k6 in k6_candidates:
                                    key = k1 + k2 + k3 + k4 + k5 + k6
                                    result = decrypt(cyphertext, key)
                                    if result != False:
                                        myfile.write("Klucz: " + key + " Tekst: " + result + "\n")

if __name__ == "__main__":
    main()