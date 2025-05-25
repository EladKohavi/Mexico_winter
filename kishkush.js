
function isEven(num: number) {
  if (num % 2 == 0) {
    return true;
  }
  // Missing return statement
}

console.log("merge Bug?", isEven(5));
console.log("merge Bug?");
console.log("merge Bug?");
console.log("merge Bug?");
