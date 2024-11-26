text_with_space = "  Ryan Clarke  "
text_wthout_space = text_with_space.strip()
print(text_wthout_space)

text_with_brackets = "(Ryan Clarke)"
text_without_brackets = text_with_brackets.strip('(')
text_without_brackets =text_without_brackets.strip(')')
print(text_without_brackets)