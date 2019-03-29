// If the number is positive it returns yes otherwise the function specifies what kind of error it was (negative or zero)
function isPositive(a) {
    if (a == 0) {throw new Error("Zero Error") }
    if (a < 0) { throw new Error("Negative Error") }
    return "YES"
}
