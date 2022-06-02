function solution(n, lost, reserve) {
  let filtered_lost = lost.filter( x => !reserve.includes(x));
  let filtered_reserve = reserve.filter( x => !lost.includes(x));
  filtered_lost = filtered_lost.sort((a,b)=>{return a-b})
  filtered_reserve = filtered_reserve.sort((a,b)=>{return a-b})
  let answer = n-filtered_lost.length;
  filtered_lost.forEach( num =>{
      if(filtered_reserve.includes(num-1)){
          filtered_reserve = filtered_reserve.filter( element => element !== (num-1));
          answer+=1
      }else if(filtered_reserve.includes(num+1)){
          filtered_reserve = filtered_reserve.filter( element => element !== (num+1));
          answer+=1
      }else{
          answer+=0
      }
  })
  return answer;
}

//  차집합, 정렬, includes, forEach