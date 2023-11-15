
list1 = ['hello', 'word', 'school', 'Python', 'php', 'go', 'hi', 'C']
list2 = ['Python', 'php', 'go', 'C', '1234']

print(list([word for word in list1 if word in list2]))