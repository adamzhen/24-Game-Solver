def op(n, n1, n2):
  if n==0:
    return n1+n2
  elif n==1:
    return n1-n2
  elif n==2:
    return n1*n2
  elif n==3:
    if n2!=0:
      return n1/n2
    else:
      return 99999
def opsymb(n):
  if n==0:
    return '+'
  elif n==1:
    return '-'
  elif n==2:
    return '*'
  elif n==3:
    return '/'
def check24(cnums):
  tfs, three, two, one = [], [], [], []
  three.append(cnums[0])
  three.append(cnums[1])
  two.append(cnums[0])
  for i in range(4):
    three.append(op(i, cnums[2], cnums[3]))
    for h in range(4):
      two.append(op(h, three[1], three[2]))
      for j in range(4):
        one.append(op(j, two[0], two[1]))
        if one[0]==24:
          tfs.append([i,h,j])
        one.pop()
      two.pop()
    three.pop()
  return tfs
def addans(answers, equations):
  if len(equations)>0:
    for i in range(len(equations)):
      answers.append(equations[i])
  return answers
def printans(ans, cnums):
  equations=[]
  if len(ans)>=1:
    for i in range(len(ans)):
      tnums=[]
      for j in range(len(cnums)):
        tnums.append(str(cnums[j]))
      ops=ans[i]
      tnums.insert(1,opsymb(ops[2]))
      tnums.insert(3,opsymb(ops[1]))
      tnums.insert(5,opsymb(ops[0]))
      tnums.insert(7,")")
      tnums.insert(8,")")
      tnums.insert(4,"(")
      tnums.insert(2,"(")
      tnums.append("=")
      tnums.append("24")
      equations.append("".join(tnums))
  return equations
play="y"
print("\nGAME OF 24")
while play=="y":
    total=0
    cnums, answers=[], []
    while True:
        try:
            nums=input('\nEnter 4 integers separated by spaces(format: n1 n2 n3 n4): ').split(" ")
            break
        except:
            print("Please enter 4 integers in this format: n1 n2 n3 n4: ")
    for i in range(len(nums)):
        nums[i]=int(nums[i])
    for i in range(4):
        cnums.append(nums[i])
        for h in range(3):
            indxs=list(range(4))
            if i+h+1>3:
                cnums.append(nums[i+h+1-4])    
                indxs[i+h+1-4]=5
            else:
                cnums.append(nums[i+h+1])
                indxs[i+h+1]=5
            for j in range(2):
              indxs[i]=5
              remn=[]
              for k in range(len(indxs)):
                if indxs[k]!=5:
                   remn.append(indxs[k])
              cnums.append(nums[remn[j]])
              cnums.append(nums[remn[j-1]])
              total+=len(check24(cnums))
              equations=printans(check24(cnums), cnums)
              answrs=addans(answers, equations)
              cnums.pop()
              cnums.pop()
            cnums.pop()
        cnums.pop()
    if total==0:
      print("There is no way to get 24.")
    else:
      answers=list(set(answers))
      print("SOLUTIONS:")
      for i in range(len(answers)):
        print(answers[i])
    play=input("Do you want to go again? y/n: ")
print("Thanks for using Game of 24!")

