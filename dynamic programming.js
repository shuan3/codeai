function fibonacci(n){
    let cache={0:0,1:1,2:1};
    if (n in cache){
        return cache[n];
    }else{
        console.log("Taking long time.Calculating Fibonacci for:", n);
        cache[n]=fibonacci(n-1)+fibonacci(n-2);
        return n<=1 ? n : fibonacci(n-1)+fibonacci(n-2);
    }
}



// can be divided into smaller subproblems
// recursive structure
// overlapping subproblems
//memorize the results of subproblems to avoid redundant computations
//are there common subproblems that are solved multiple times?