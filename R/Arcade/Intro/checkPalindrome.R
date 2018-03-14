checkPalindrome <- function(inputString) {
  inputString <- unlist(strsplit(inputString, ""))
  all(inputString == rev(inputString))
}
