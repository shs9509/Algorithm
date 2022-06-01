function solution(array, commands) {
  let answer = [];
  let tmp =[];
  commands.forEach( command =>{
      let [start, end, target] = command
      // let start, end, target = command 이건 안된다리
      tmp = array.slice(start-1,end)
      console.log(tmp)
      // tmp.sort(function(a,b){
      //     return a-b
      // })
      tmp.sort((a,b)=>a-b)
      answer.push(tmp[target-1])
  })
  return answer;
}
// forEach, sort(), slice, 구조분해할당