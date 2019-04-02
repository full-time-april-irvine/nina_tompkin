function removeDuplicates(arr){
    for (var i = 0; i < arr.length - 1; i++){
        if (arr[i] == arr[i+1]){
            console.log("The array is currently "+arr+".");
            for (var j = i+1; j < arr.length-1; j++){
                arr[j] = arr[j+1];
                console.log("The array is currently "+arr+".");
            }
            arr.length--;
            i--
        }
    }
    return arr;
}

testArray = [0,1,2,3,5,7,9,9,9,10,13,13,14,14,15];

console.log(removeDuplicates(testArray));