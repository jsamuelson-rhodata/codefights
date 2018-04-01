def longestDigitsPrefix(inputString):
    return re.findall('^\d*',inputString)[0]
