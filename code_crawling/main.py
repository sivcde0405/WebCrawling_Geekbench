import time
from intro import introprog
from readcell import readCPUlist
from readcell import makeScorelist
from readcell import makeCPUlist
from readcell import makeTestlist
from crawling import crawlpage
from crawling import crawlbenchlen
from calculating import calcavg
from writecell import listtoxlsx

dointroload = 1

if(dointroload == 1):
    introprog()
else:
    print('now loading DB (0%)')

CPU_RAWlist = readCPUlist()
print('now loading DB (33%)')
CPU_list = makeCPUlist()
CPU_test_list = makeTestlist()
print('now loading DB (67%)')
Score_list = makeScorelist()
print('now loading DB (100%)')
time.sleep(0.5)

#print(CPU_list)
#print('\n----\n')
#print(Score_list)
print('\n\n---now start crawling---')
time.sleep(0.5)

for i in range(12):#12
    for j in range(1, 5):#(1, 6)
        if (CPU_list[i][j] != None):
            print(f'start crawling \"{CPU_list[i][j]}\"')
            #print(' ')
            CPU_scoreST = []
            CPU_scoreMT = []
            CPU_score = []

            benchlen = crawlbenchlen(CPU_list[i][j], 1) // 25
            benchpage = min(benchlen+1, 31)
            for k in range(1, benchpage):#(1, 31)
                print(f'\rnow crawling {k} / {benchpage} page', end = "")
                CPU_score.extend(crawlpage(CPU_list[i][j], k))
            print(f'\rnow appending page', end="")
            for k in range(len(CPU_score)):
                CPU_scoreST.append(CPU_score[k][0])
                CPU_scoreMT.append(CPU_score[k][1])

            mylist = [calcavg(CPU_scoreST), calcavg(CPU_scoreMT)]
            '''
            print(CPU_score)
            print(CPU_scoreST)
            print(CPU_scoreMT)
            print(mylist)
            '''
            print(f'\rCPU \"{CPU_list[i][j]}\"s Score is {mylist} : searched {benchpage} / {max(30, benchlen)} page')
            #print(f'end crawling \"{CPU_list[i][j]}\"')
            Score_list[i][j] = mylist
            CPU_test_list[i][j] = max(30, benchlen)

#print(Score_list)
Score_list_ST = []
Score_list_MT = []
Score_list_ST.append(['Generation', 'i9', 'i7', 'i5', 'i3'])
Score_list_MT.append(['Generation', 'i9', 'i7', 'i5', 'i3'])
for i in range(12):
    print(f'now writing DB ({100*i/12}%)')
    time.sleep(0.05)
    mylist_ST = []
    mylist_MT = []
    mylist_ST.append(i+1)
    mylist_MT.append(i+1)
    for j in range(1, 5):
        mylist_ST.append(Score_list[i][j][0])
        mylist_MT.append(Score_list[i][j][1])
    Score_list_ST.append(mylist_ST)
    Score_list_MT.append(mylist_MT)

print('now writing DB (100%)')
'''
print(Score_list_ST)
print('\n----\n')
print(Score_list_MT)
'''
listtoxlsx(Score_list_ST, 'STScore.xlsx')
listtoxlsx(Score_list_MT, 'MTScore.xlsx')
listtoxlsx(CPU_test_list, 'Test_repeat.xlsx')

print('END!')
print('now closing..')
time.sleep(3)