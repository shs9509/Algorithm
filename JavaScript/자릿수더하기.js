// https://programmers.co.kr/learn/courses/30/lessons/12931
function solution(n)
{
    let V = String(n).split("").reduce(function add(sum,curVal){
        return Number(sum)+Number(curVal);
    },0)
    return V;
}

function solution(n)
{
    var sum =0;
    do{
        sum +=n%10;
        n=Math.floor(n/10);
    }while(n>0);
    return sum;
}