# def shift_letters(sentence):
#     words = sentence.split()
#     shifted_words = []
    
#     for i in range(len(words)):
#         if i == len(words) - 1:
#             shifted_word = words[0][0] + words[i][1:]
#         else:
#             shifted_word = words[i][1:] + words[i+1][0]
#         shifted_words.append(shifted_word)
    
#     return ' '.join(shifted_words)

# sentence = input()
# print(shift_letters(sentence))

# def shift_letters(sentence):
#     words = sentence.split()
#     shifted_words = []
    
#     for i in range(len(words)):
#         if i==0:
#             newWord=words[-1][0]+words[1:]
#             shifted_words.append(newWord)
#         else:
#             newWord =words[i+1][0]+words[i][1:]
#             shifted_words.append(newWord)
#     return ' '.join(shifted_words)

# sentence = input()
# print(shift_letters(sentence))

def shift_letters(sentence):
    words = sentence.split()
    shifted_words = []

    for i in range(len(words)):
        shifted_word = words[i - 1][0] + words[i][1:]
        shifted_words.append(shifted_word)    
    return ' '.join(shifted_words)

sentence = input()
print(shift_letters(sentence))
