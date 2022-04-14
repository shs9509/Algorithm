# https://programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = []
    reported_time={}
    report_people={}
    report = list(set(report))
    for j in id_list:
        reported_time[j]=0
        report_people[j]=[]
    for i in report:
        person1, person2 = i.split(' ')
        reported_time[person2]+=1
        report_people[person1].append(person2)
        
    for m in report_people:
        count =0
        for l in report_people[m]:
            if reported_time[l]>=k:
                count+=1
        answer.append(count)
                
    return answer