/*
Imagine -- Mai Rachlevsky, Qian Zhou
SoftDev1 pd07
K28 -- Sequential Progression
2018-12-18
*/

/* factorial */
var fact=function(n){
  if (n<2){
    return 1;
  }
  else{
    return n*fact(n-1);
  }
};

/* fibbonaci number */
var fibbonaci = (n)=>{
    if (n<2)
	return n;
    else{
	return fibbonaci(n-2) + fibbonaci(n-1);
    }
};

/* greatest common demoniator, Euclidean algorithm??? */
var gcd = (a,b) =>{
    if (b!=0)
	return gcd(b,a%b);
    else{
	return a;
    }
};

/* define a list for convenience */
var students = ['ananke', 'boule', 'irene', 'metron', 'ho polemos', 'philos','pratto', 'pisteuo', 'erchomai'];

/* input list, returns a random element */
var randomStudent = (list) =>{
    index = parseInt(Math.random()*list.length);
    return list[index];
};
    
    
