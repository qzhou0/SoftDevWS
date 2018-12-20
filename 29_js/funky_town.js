/*
Jared Asch, Qian Zhou
SoftDev1 pd07
K29 -- Sequential Progression II: Electric Boogaloo...
2018-12-19
*/

/* ===============================K 28 from myself ======================== */
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
    

/*============================K29 =====================*/

var p_tag = document.getElementById("results");// from JL's QAF post, write in html

// buttons and eventListeners

fibBtn = document.getElementById("fib");
fibBtn.addEventListener('click', function (){
    console.log(fibbonaci(10));
    p_tag.innerHTML = String(fibbonaci(10));
});

gcdBtn = document.getElementById("gcd");
gcdBtn.addEventListener('click', function(){
    console.log(gcd(3153, 120));
    p_tag.innerHTML = gcd(3153, 120);
});

randBtn = document.getElementById("rand_student");
randBtn.addEventListener('click', function(){
    console.log(randomStudent(students));
    p_tag.innerHTML = randomStudent(students);
});
