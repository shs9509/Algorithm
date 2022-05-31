// https://programmers.co.kr/learn/courses/30/lessons/76501?language=javascript
function solution(absolutes, signs) {
  let answer = 0;
  for(i=0;i<absolutes.length;i++){
      if(signs[i]){
          answer+=absolutes[i]
      }else{
          answer-=absolutes[i]
      }   
  }
  return answer
}