rows = int(input())
for i in range(rows):
  for j in range(i + 1):
    print(j + 1,
          end="")  #end ="" means the output should end with an empty string
  print("")
