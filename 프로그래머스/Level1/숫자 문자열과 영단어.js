// function solution(s) {
//     let answer = [];
//     let num_check = /[0-9]/;
//     let eng_check = /[a-zA-Z]/;
//     let li = s.split('');
//     let tmp =''
//     li.forEach( i =>{
//         if(eng_check.test(i)){
//             tmp+=i
//         }else{
//             answer.push(i)
//         };
//         if(tmp=='one'){
//             answer.push(1);
//             tmp=''
//         }else if( tmp =='two'){
//             answer.push(2);
//             tmp=''
//         }else if( tmp =='three'){
//             answer.push(3);
//             tmp=''
//         }else if( tmp =='four'){
//             answer.push(4);
//             tmp=''
//         }else if( tmp =='five'){
//             answer.push(5);
//             tmp=''
//         }else if( tmp =='six'){
//             answer.push(6);
//             tmp=''
//         }else if( tmp =='seven'){
//             answer.push(7);
//             tmp=''
//         }else if( tmp =='eight'){
//             answer.push(8);
//             tmp=''
//         }else if( tmp =='nine'){
//             answer.push(9);
//             tmp=''
//         }else if( tmp =='zero'){
//             answer.push(0);
//             tmp=''
//         }
//     })
//     return +answer.join('');
// }
function solution(s) {
  let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  var answer = s;

  for(let i=0; i< numbers.length; i++) {
      let arr = answer.split(numbers[i]);
      answer = arr.join(i);
  }

  return Number(answer);
}