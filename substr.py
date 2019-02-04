def substr(s, c, n):
# @param s : str
# @param c : str
# @param n : int
# @return bool
  assert len(c) == 1
  
  if n <= 0:
    return True
  elif not len(s):
    return False
  
  if s[0] == c:
    return substr(s[1:], c, n - 1)
    
  return substr(s[1:], c, n)