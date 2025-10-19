function fibonacci(n){
    let cache={0:0,1:1,2:1};
    if (n in cache){
        return cache[n];
    }else{
        console.log("Taking long time. Calculating Fibonacci for:", n);
        return n<=1 ? n : fibonacci(n-1)+fibonacci(n-2);
    }
}