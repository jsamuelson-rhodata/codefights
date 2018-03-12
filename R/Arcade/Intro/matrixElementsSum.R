matrixElementsSum <- function(m) {
  m <- matrix(unlist(m), nrow = length(m), byrow = TRUE)
  set0 <- function(x) if (any(x == 0)) c(x[1:which.max(x == 0)], rep(0, length(x) - which.max(x == 0))) else x
  sum(apply(m, 2, set0))
}
