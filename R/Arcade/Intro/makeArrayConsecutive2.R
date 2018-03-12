makeArrayConsecutive2 <- function(statues) {
  statues <- unlist(statues)
  length(min(statues):max(statues)) - length(statues)
}
