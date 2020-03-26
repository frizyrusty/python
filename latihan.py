# eventStart=14
# eventEnd=21
# events=[1,2,4,5]
# availA=[14,15,16]
# availB=[15,17]
# availC=[14]
# dateA=[]
# dateB=[]
# dateC=[]
# dateAll=[]
# dateAvailable=[]
# for indeks in range(eventStart, eventEnd + 1):
#     dateAll.append(indeks);
    
# # print(dateAll)

# for num in events:
#     dateAvailable.append(dateAll[num - 1])

# # print(dateAvailable)

# for date in availA:
#     if int(date) in dateAvailable:
#         dateA.append(date)

# for date in availB:
#     if int(date) in dateAvailable:
#         dateB.append(date)
        
# for date in availC:
#     if int(date) in dateAvailable:
#         dateC.append(date)
        
# print('A: ' + ' '.join(map(str, dateA)))
# print('B: ' + ' '.join(map(str, dateB)))
# print('C: ' + ' '.join(map(str, dateC)))



array = []
for i in range(1, 100):
    # print(i)
    if i  % 2 == 0:
        array.append(2)
    elif i % 3 == 0:
        array.append(3)
    else :
        array.append(0)
print(array)
print(sum(array))