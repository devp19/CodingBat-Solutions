public String front22(String str) {
  
  String first2 = str;
  
  if (str.length()>2) {
    first2 = str.substring(0,2);
  }
 
  return(first2 + str + first2);
}
