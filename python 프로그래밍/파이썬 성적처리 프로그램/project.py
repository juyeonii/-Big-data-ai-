#!/usr/bin/env python
# coding: utf-8

# # 성적 관리 프로그램

# #### 문제
# 파일로부터 데이터를 읽어서 성적 목록을 만들어 관리하는 성적 관리 프로그램을 작성한다

# In[ ]:


import os

#파일 불러오기
import sys
arg = sys.argv
if len(sys.argv)==1:
    file="students.txt"
else:
    file=sys.argv[1]
fr=open("students.txt","r")


    
#학점 나누는 함수
def grade(x):
    if x>=90: grade="A"
    elif x>=80: grade="B"
    elif x>=70: grade="C"
    elif x>=60: grade="D"
    else: grade="F"
    return grade

#리스트로 저장
stu_list=[]
for i in fr:
    s_split=i.split()
    new=(s_split[1]+" "+s_split[2])#성이랑 이름을 합침
    s_split.append((int(s_split[3])+int(s_split[4]))/2)
    s_split.append(grade(s_split[5]))
    new_student=[s_split[0],new,s_split[3],s_split[4],s_split[5],s_split[6]]
    stu_list+=[new_student]


#평균 점수를 기준으로 내림차순 정렬
stu_list.sort(key=lambda e : e[4], reverse = True)


#show(전체 학생 정보 출력-평균 점수를 기준으로 내림차순)
def show(list1):
    print("Student          Name        Midterm   Final   Average Grade")
    print("-"*60)
    list1.sort(key=lambda e : e[4], reverse = True)
    for i in list1:
        for j in i:
            print(j,end="\t")
        print("")
    print()
    return

#search(특정 학생 검색)
def search(list1):
    Id=input("Student ID: ")
    for i in range(len(list1)):
        if list1[i][0]==Id:
            print("Student          Name        Midterm   Final   Average Grade")
            print("-"*60)
            for j in list1[i]:
                print(j,end="\t")
            return
    print("No SUCH PERSON.")
    print()
    return

#changescore(점수 수정)
def changescore(list1):
    Id=input("Student ID: ")
    for i in range(len(list1)):
        if list1[i][0]==Id:
            score=input("Mid/Final? ")
            if score=="mid":
                new_score=int(input("Input new score: "))
                if new_score<=100 and new_score>=0:
                    print("Student          Name        Midterm   Final   Average Grade")
                    print("-"*60)
                    for j in list1[i]: print(j,end="\t")
                    print()
                    print("Score changed.")
                    list1[i][2]=int(new_score)
                    list1[i][4]=(list1[i][2]+int(list1[i][3]))/2
                    list1[i][5]=grade(list1[i][4])
                    for j in list1[i]:
                        print(j,end="\t")
                    return
                else: return
            
            elif score=="final":
                new_score=int(input("Input new score: "))
                if new_score<=100 and new_score>=0:
                    print("Student          Name        Midterm   Final   Average Grade")
                    print("-"*60)
                    for j in list1[i]: print(j,end="\t")
                    print()
                    print("Score changed")
                    list1[i][3]=int(new_score)
                    list1[i][4]=(int(list1[i][2])+list1[i][3])/2
                    list1[i][5]=grade(list1[i][4])
                    for j in list1[i]:
                        print(j,end="\t")
                    return
                else: return
            else:return

    print("NO SUCH PERSON")
    print()

#add(학생 추가)
def add(list1):
    Id=input("Student ID: ")
    for i in range(len(list1)):
        if list1[i][0]==Id:
            print("ALREADY EXISTS.")
            return
    
    name=input("Name: ")
    m=int(input("Midterm Score: "))
    f=int(input("Final Score: "))
    g=(m+f)/2
    s=[Id,name,m,f,g,grade(g)]
    list1+=[s]
    print("Student added.")
    print()
#searchgrade(Grade 검색)
def searchgrade(list1):
    a=["A","B","C","D","F"]
    count=0
    grade=input("Grade to search: ")
    grade_result=[]
    if grade in a:
        for i in range(len(list1)):
            if list1[i][5]==grade:
                count+=1
                grade_result.append(list1[i])
        if count==0:print("NO RESULTS.")
        else:
            print("Student          Name        Midterm   Final   Average Grade")
            print("-"*60)
            for i in range(len(grade_result)):
                for j in grade_result[i]:   
                    print(j,end="\t")
                print("\n")
    print()          
#REMOVE(특정 학생 삭제)
def remove(list1):
    if len(list1)>0:
        Id=input("Student ID: ")
        for i in range(len(list1)):
            if list1[i][0]==Id:
                list1.remove(list1[i])
                print("Student removed.")
                return
        print("NO SUCH PERSON.")
        
    else:print("List is empty.")
    print()  
#quit(종료)
def quit(list1):
    save=input("Save data?[yes/no] ")
    if save=="yes":
        file=input("File name: ")
        print("$")
        fw=open(file,"w")
        list1.sort(key=lambda e:e[4],reverse=True)
        fw.write("Student    Name    Midterm   Final   Average Grade")
        fw.write("\n")
        fw.write("-"*45)
        fw.write("\n")
        for i in list1:
            temp=str(i[0])+"\t"+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+"\t"+str(i[4])+'\t'+str(i[5])+'\n'
            fw.write(temp)
        fr.close()    
        fw.close()
    else:print("$")
    print()



while True:
    command = input("# ")             
    if command.lower() == "show": show(stu_list)   
    elif command.lower() == 'search':search(stu_list)
    elif command.lower() == 'changescore':changescore(stu_list)
    elif command.lower() == 'add':add(stu_list)
    elif command.lower() == 'searchgrade':searchgrade(stu_list)
    elif command.lower() == 'remove':remove(stu_list)
    elif command.lower() == "quit":quit(stu_list)
    else:continue


# In[ ]:





# In[ ]:




