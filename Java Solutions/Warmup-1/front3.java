public String front3(String str) {
  
  if (str.length() >= 3) {
    String first3 = str.substring(0, 3);
    
    return(first3 + first3 + first3);
  }
  else{
  return(str + str + str);
  }
  
}
