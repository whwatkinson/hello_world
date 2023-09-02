# Given a string str, find the length of the longest substring without repeating characters.
# For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.


# def stirng_has_unique_chars(string_in: str) -> bool:

#     if len(string_in) == len(set(string_in)):
#         return True

#     return False


# def find_longest_substring(string_in: str) -> str:

#     sub_string_list = []
#     count = 0
#     longest_sub_sting = ""

#     for char in string_in:
#         count += 1
#         longest_sub_sting += char

#         if stirng_has_unique_chars(longest_sub_sting):
#             sub_string_list.append(longest_sub_sting)
#             continue
#         else:
#             longest_sub_sting = char
#             coint

#     length_of_sub_strings =  [len(x) for x in sub_string_list]

#     return sorted(length_of_sub_strings, key=lambda x: x, reverse=True)[0]


# print(find_longest_substring("ABDEFGABEF"))


def find_longest_substring(s):
    char_set = set()
    max_length = 0
    inter_length = 0
    for char in s:
        if char in char_set:
            max_length = max(max_length, inter_length)
            char_set = set()
            inter_length = 0
        char_set.add(char)
        inter_length += 1
    return max(max_length, inter_length)


print(find_longest_substring("ABDEFGABEF"))

