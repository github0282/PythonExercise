
list1 = [10, 20, 4, 45, 99]
  
x=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
print("the list is : " , list1)
for i in range(2,n):
    if list1[i]>x:
        secondmax=x
        x=list1[i]
    elif list1[i]>secondmax and \
        x != list1[i]:
        secondmax=list1[i]

print("Second highest number is : ", \
      str(secondmax))

list = [1, 2, 3, 4, 5]
print("the old list is : ", list)
f = list[0]
l = list[-1]
list[-1] = f
list[0] = l
print("The new list is : ", list)


test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list before duplicate number removal : " +  str(test_list))
res = []
for i in test_list:
    if i not in res:
        res.append(i)
print ("The list after removing duplicates : " + str(res))



def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["Python", "Exercises", "Program"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])