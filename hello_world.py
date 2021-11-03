print('hello world')

# for i in range (2,100,2):
  #  print(i)

#for i in range (1,100,2):
 #   print(i)


for i in range(1,100):
    primo = True
    for j in range (2,9):
        if i % j == 0 and i != j:
            primo = False
            #print(i, j, 'no primo')
    if primo:
        print('primo', i)

## mauricio reyes orozco credential store 2
