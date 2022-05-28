// https://programmers.co.kr/learn/courses/30/lessons/77484?language=javascript
function solution(lottos, win_nums) {
  let answer = [];
  let count = 0
  let zero_count = lottos.map( num => {
      if(num==0){
          count +=1
      }
  })
  let correct = lottos.filter(lotto => win_nums.includes(lotto));
  answer.push(7-correct.length-count);
  answer.push(7-correct.length);
  answer = answer.map(x => {
      if(x==7){
          return 6
      }else{
          return x
      }
  })
  return answer;
}