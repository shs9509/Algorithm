// https://programmers.co.kr/learn/courses/30/lessons/12944
function solution(arr) {
  const result = arr.reduce(function add(sum,curValue){
      return sum + curValue;
  },0)
  const average = result / arr.length;
  return average
}