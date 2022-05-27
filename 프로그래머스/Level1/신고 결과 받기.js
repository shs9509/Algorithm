// https://programmers.co.kr/learn/courses/30/lessons/92334?language=javascript
function solution(id_list, report, k) {
  let answer = [];
  report = [...new Set(report)];
  // const reported = report.map(el => el.split(' ')[1]);
  let reports = [ ...new Set(report) ]
  let reported_people = {};
  let reporting_count = {};
  id_list.forEach((id) =>{
      reported_people[id] = [];
      reporting_count[id] = 0;
  })
  reports.forEach((repo) =>{
      let [one,two] = repo.split(' ');
      reported_people[two].push(one);
  })
  id_list.forEach((person) => {
      if (reported_people[person].length >=k){
          reported_people[person].forEach((reporting_person) => {
              reporting_count[reporting_person]+=1;
          })
      }
  })
  for(let person in reporting_count){
      answer.push(reporting_count[person]);
  }
  return answer;
}