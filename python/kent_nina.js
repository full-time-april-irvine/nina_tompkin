//Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr ’s values to th e right by that amount. ‘Wrap-around’ any values that shift off array’s end to the other side, s o that no data is lost. Operate in-place: given ([1,2,3],1) , change the array to [3,1,2] . Don’ t use built-in functions . Second: allow negative shiftBy (shift L, not R) . Third: minimize memory usage. With no new array, handle arrays/ shiftBy s in the millions . Fourth: minimize the touches of each element .


y = rotateArrNeg([1,2,3,4,5],-1); 
x = rotateArrNeg([1,2,3,4,5],-2);

console.log(y)
console.log(x)
    


function rotateArr(arr, shiftBy){
    for (j = 1; j <= shiftBy; j++){
        temp = arr[arr.length - 1]
        for (i = arr.length - 1; i > 0 ; i--){
            arr[i] = arr[i -1];
        }
        arr[0] = temp;
  }
    return arr;
}

testArr = [1,2,3,4,5],2
    

y = rotateArr([1,2,3,4,5],1);
x = rotateArr([1,2,3,4,5],2);

console.log(y)
console.log(x)
