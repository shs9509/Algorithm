function solution(n) {
  let V = String(n).split("").reduce(function push(arr,cur){
      arr.push(Number(cur))
      return arr
  },[]).reverse();
  return V
}

// function solution(n) {
//     let V = String(n).split("").map((str)=>Number(str)).reverse();
//     return V
// }