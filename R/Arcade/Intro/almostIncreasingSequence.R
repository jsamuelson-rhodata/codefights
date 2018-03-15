almostIncreasingSequence <- function(s) {
  s <- unlist(s)
  n <- length(s)
  
  if (n > 2) 3 > sum(s[1:(n-1)] >= s[2:n]) + sum(s[1:(n-2)] >= s[3:n]) else TRUE
}
