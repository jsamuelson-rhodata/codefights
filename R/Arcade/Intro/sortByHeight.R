sortByHeight <- function(a) {
  a <- unlist(a)
  a[a > 0] <- sort(a[a > 0])
  as.list(a)
}
