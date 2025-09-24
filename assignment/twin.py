def twin(text,i,j,count):
    # base case
    if i >= len(text) or j >= len(text):
        return
    # recursive case
    if text[i] == text[j]:
        count.append(1)

    twin(text,i+1,j+1,count)
       

    

text = input()
count = []
twin(text,0,2,count)
print(sum(count))