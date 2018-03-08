with open ('file2','r') as file1:
    with open('file1','r') as file2:
        same=set(file2).difference(file1)
        same.discard('\n')
        print(same)
