"'
Author sample code from Dbrmarie
july13
scrable a sentence and print it
"'
import random
def main():
  sent = input("Enter a sentence to scramble: ")
  new_sentence = scramble(sent)
  print(new_sentence)
def scramble(sentence):
  word_list = sentence.split(" ")
  for x in range(5):
    random.shuffle(word_list)
  new_list = [ word.lower() for word in word_list ]
  other_sent = " ".join(new_list)
  return other_sent
main()
