commonCharacterCount <- function(s1, s2) sum(is.finite(pmatch(strsplit(s1, NULL)[[1]], strsplit(s2, NULL)[[1]])))
