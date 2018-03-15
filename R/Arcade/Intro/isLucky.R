isLucky <- function(n) {
  n <- as.integer(strsplit(as.character(n), NULL)[[1]])
  d <- length(n)
  sum(n[1:floor(d / 2)]) == sum(n[(floor(d / 2) + 1):d])
}
