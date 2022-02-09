# Don't change code above 👆
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Write your code below:
print(sentence.split())
letter_numbers = [ len(number) for number in sentence.split()]
result = dict(zip(sentence.split(),letter_numbers))
result = {word:len(word) for word in sentence.split()}

print(result)
