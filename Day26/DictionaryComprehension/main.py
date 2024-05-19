sentence = input()

# Using dictionary comprehension
result = {word:len(word) for word in sentence.split()}

print(result)