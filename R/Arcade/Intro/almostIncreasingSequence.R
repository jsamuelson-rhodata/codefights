almostIncreasingSequence <- function(sequence) {
  sequence <- unlist(sequence)
  n <- length(sequence)
  
  if (n > 2) {
    3 > sum(sequence[1:(n-1)] >= sequence[2:n]) + sum(sequence[1:(n-2)] >= sequence[3:n])
  } else {
    TRUE
  }
}
