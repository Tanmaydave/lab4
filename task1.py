import string

def vocabulary_counter(a_file, start_line=1):
    new_text = []
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[start_line - 1:]

    for line in lines:
        stripped_line = line.strip().lower().translate(string.maketrans("",""), string.punctuation).split()
        new_text += stripped_line


    word_count_dict = {}
    for word in new_text:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    total_words = len(new_text)
    num_different_words = len(word_count_dict.keys())
    varied_vocab_percent = float(num_different_words) / total_words

    print ("Total number of words: " + str(total_words) + "\n" + "Number of different words: " + str(num_different_words) + "\n" + "Vocab Variance Percent: " + str(varied_vocab_percent))