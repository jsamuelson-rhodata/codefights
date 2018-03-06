checkPalindrome <- function(inputString) {
  s <- unlist(strsplit(inputString, ""))
  all(s == rev(s))
}