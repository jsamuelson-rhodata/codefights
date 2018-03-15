reverseParentheses <- function(s) {
  s <- strsplit(s, NULL)[[1]]
  while (")" %in% s) {
    i <- max(which(s == "("))
    j <- i + min(which(s[(i+1):length(s)] == ")"))
    s[i:j] <- s[j:i]
    s <- s[-c(i,j)]
  }
  paste(s, collapse = "")
}
