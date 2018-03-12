adjacentElementsProduct <- function(inputArray) {
  inputArray <- unlist(inputArray)
  n <- length(inputArray)
  max(inputArray[1:(n-1)] * inputArray[2:n])
}
