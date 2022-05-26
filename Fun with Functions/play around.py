# number = int(input("Enter a Number: "))
# square_root = round(number ** (1.0 / 2))
#
# divisor_list = []
# for i in range(1, square_root+1):
#     if number % i == 0: # Check if mod return 0 if yes then append i and number/i in the list
#         divisor_list.append(i)
#         divisor_list.append(int(number/i))
#
# print(divisor_list)

# def divisors(n):
#     result = []
#     for i in range(1, n//2 + 1):
#         if n % i == 0:
#             result.append(i)
#     result.append(n)
#     return result
# print(divisors(44))

# def is_factor(f, n):
#     return n%f==0

# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
# # A2a:
# #for x in alphabet:
#    # print(dict[x])
# def alpha(x):
#     index = 0
#     for x in alphabet:
#         d = (dict[alphabet[index]])
#     index = index + 1
#
# print(x)
# def alphabet_position(text):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
#                 "v", "w", "x", "y", "z", " "]
#     arr = []
#     new_text = text.lower()
#     for i in list(new_text):
#         for k, j in alphabet.iteritems():
#             if k == i:
#                 arr.append(j)
#         print(' '.join(arr))

# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
# # # A2a:
# # for x in alphabet:
# #     print(int(x))
#
# def products(alp):
#     result = 0
#     for x in alphabet:
#         result *= alphabet.index("t")
#     return result
# print(products(4))

# def alpha_letter(letter):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
#                 "v", "w", "x", "y", "z", " "]
#
#     return alphabet.index(letter)
#
# def index_name(word):
#     index = []
#     for i in word:
#         x = alpha_letter((i).lower())
#
#         index.append(x + 1)
#
#     newString = ''.join(str(index))
#     return newString
#
#
# print(index_name("Ade"))


# def name_index(name):
#     index = []
#     id_number = ""
#     for char in name:
#         find = alpha_letter(char)
#         index.append(find)
#     id_number = "".join(index)
#     return id_number
# print(name_index("hello"))