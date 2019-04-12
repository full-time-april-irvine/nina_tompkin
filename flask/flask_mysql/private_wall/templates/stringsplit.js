function stringSplit(str,separator,limit){
    //We'll use an array to store all the things we want.
    arr = [];
    //We'll use a string to temporarily keep track of the characters we've gone over (and want) so far.
    newstr="";
    //Loop through the entire string length
    for (var i = 0; i < str.length; i++){
        //If we come across something that is not our separator (aka things we want)
        if (str[i] != separator){
            //Append our newstring with the value of of what we want
            newstr += str[i];
        }
        else{
            //otherwise...if we come across a separator, then we want to grab the value of the "chunk" we came across prior, and put it into the array to save it.
                arr.push(newstr);
                //Then, we're going to 
                if (arr.length >= limit){
                    return arr;
                }
                newstr = "";
            }
    }
    //Then, once we reach the end, put the last chunk of the string into it
    arr.push(newstr);
    return arr;
}
    

var str = 'The quick brown fox jumps over the lazy dog.';
console.log(stringSplit(str," ",99));

// otherstr = "This: Is the final: frontier";

// console.log(stringSplit(otherstr,":"));

