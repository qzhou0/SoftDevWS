/*
Imagine -- Mai Rachlevsky, Qian Zhou
SoftDev1 pd07
K30 -- Sequential Progression III: Season of the Witch
2018-12-20
*/

/* fibbonaci number */
var fibbonaci = (n)=>{
    if (n<2)
	return n;
    else{
	return fibbonaci(n-2) + fibbonaci(n-1);
    }
};



var h = document.getElementById('h');//heading
var tl = document.getElementById("thelist");//thelist


/* event listener adder for thelist */
var paideuetai=(i, elem)=>{
    elem[i].addEventListener('mouseover', function(){
	h.innerHTML = (this.innerHTML);//changes to this content
    });
    elem[i].addEventListener('mouseout',function(){
	h.innerHTML = 'Hello World';//changes back
    });
    elem[i].addEventListener('click',function(){
	this.remove();
	h.innerHTML = 'Hello World';//special case for changing back
    });
}
// indoctrination for the firstborn
for (i = 0; i<tl.children.length; i++){
    paideuetai(i,tl.children);
}
//create new list element
var newItem=(inn)=>{
    w= document.createElement("li");
    w.innerHTML = inn;
    return w;
}

/* the button */
var dasbut = document.getElementById('b');
dasbut.addEventListener('click', function(e){
    w = newItem("WORD");
    tl.appendChild(w);
    paideuetai(tl.children.length-1,tl.children);
    
});


/* Fibbs */
var fibs = document.getElementById("fiblist");
var fibBtn = document.getElementById("fb");
var currFibIndex = 1;
fibBtn.addEventListener('click', function (e){
    w = newItem(fibbonaci(currFibIndex));
    currFibIndex+=1;
    fibs.appendChild(w);
});
