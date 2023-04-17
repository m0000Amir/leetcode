/**
 * @param {string} 
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
    
    let a = s.split(' ');
    // console.log(a[a.length-1]);
    console.log(a);
    let j = a.length-1;
    while (a[j] != null) { 
        console.log(a[j]);// выводит 0, затем 1, затем 2
        j -= 1;
        
    }
    console.log(j);
    
    return a[a.length-1].length;
}

let s = "   fly me   to   the moon  ";
lengthOfLastWord(s)
// console.log(lengthOfLastWord(s));