function solution(numbers) {
  var answer = [];
  for(let i=0 ; i<numbers.length-1; i++){
     for(let j=i+1 ; j<numbers.length; j++){
          answer.push(numbers[i]+numbers[j]) 
      } 
  };
  let arr = answer.sort(function(a, b)  {
    return a-b
  });
  console.log(arr)
  let set = new Set(arr)
  return [...set];
}