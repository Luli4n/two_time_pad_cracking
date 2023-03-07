def a():
    real_3_letter_words = []

    with open("polskie_slowa_3_znaki.txt", "r") as f:
        for line in f:
            real_3_letter_words.extend(line.split())

    alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

    s1 = "ycf"
    s2 = "duł"
    s1_numerical = [alphabet.index(c) for c in s1]
    s2_numerical = [alphabet.index(c) for c in s2]

    with open("a.txt", "a") as myfile:
        for k1 in range(35):
            for k2 in range(35):
                for k3 in range(35):
                    key = alphabet[k1]+alphabet[k2]+alphabet[k3]
                    w1 = alphabet[(s1_numerical[0] - k1) % 35] + alphabet[(s1_numerical[1] - k2) % 35] + alphabet[(s1_numerical[2] - k3) % 35]
                    w2 = alphabet[(s2_numerical[0] - k1) % 35] + alphabet[(s2_numerical[1] - k2) % 35] + alphabet[(s2_numerical[2] - k3) % 35]
                    if w1 in real_3_letter_words and w2 in real_3_letter_words:
                        myfile.write("Klucz: " + key + " W1: " + w1 + " W2: " + w2 + "\n")
        myfile.close()

def b():
    real_6_letter_words = []

    with open("polskie_slowa_6_znakow.txt", "r") as f:
        for line in f:
            real_6_letter_words.extend(line.replace(',',' ').replace('.',' ').split())

    print(str(len(real_6_letter_words)))
    alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

    s1 = "ibyizh"
    s2 = "qwfżpę"
    s1_numerical = [alphabet.index(c) for c in s1]
    s2_numerical = [alphabet.index(c) for c in s2]

    with open("b.txt", "a") as myfile:
        for word in real_6_letter_words:
            k1_candidates = []
            k2_candidates = []
            k3_candidates = []
            k4_candidates = []
            k5_candidates = []
            k6_candidates = []
            for i in range(6):
                for j in range(35):
                    if (alphabet.index(word[i]) + j) % 35 == s1_numerical[i]:
                        if i == 0:
                            k1_candidates.append(alphabet[j])
                        elif i == 1:
                            k2_candidates.append(alphabet[j])
                        elif i == 2:
                            k3_candidates.append(alphabet[j])
                        elif i == 3:
                            k4_candidates.append(alphabet[j])
                        elif i == 4:
                            k5_candidates.append(alphabet[j])
                        elif i == 5:
                            k6_candidates.append(alphabet[j])
            for k1 in k1_candidates:
                for k2 in k2_candidates:
                    for k3 in k3_candidates:
                        for k4 in k4_candidates:
                            for k5 in k5_candidates:
                                for k6 in k6_candidates:
                                    key = k1 + k2 + k3 + k4 + k5 + k6
                                    w1 = alphabet[(s1_numerical[0] - alphabet.index(k1)) % 35] + alphabet[(s1_numerical[1] - alphabet.index(k2)) % 35] + alphabet[(s1_numerical[2] - alphabet.index(k3)) % 35] + alphabet[(s1_numerical[3] - alphabet.index(k4)) % 35] + alphabet[(s1_numerical[4] - alphabet.index(k5)) % 35] + alphabet[(s1_numerical[5] - alphabet.index(k6)) % 35]
                                    w2 = alphabet[(s2_numerical[0] - alphabet.index(k1)) % 35] + alphabet[(s2_numerical[1] - alphabet.index(k2)) % 35] + alphabet[(s2_numerical[2] - alphabet.index(k3)) % 35] + alphabet[(s2_numerical[3] - alphabet.index(k4)) % 35] + alphabet[(s2_numerical[4] - alphabet.index(k5)) % 35] + alphabet[(s2_numerical[5] - alphabet.index(k6)) % 35]
                                    if w2 in real_6_letter_words:
                                        myfile.write("Klucz: " + key + " W1: " + w1 + " W2: " + w2 + "\n")

        myfile.close()

def main():
    a()
    b()

if __name__ == "__main__":
    main()
    








