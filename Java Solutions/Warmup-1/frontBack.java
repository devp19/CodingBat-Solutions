public String frontBack(String str) {
  
  if(str.length() > 1){
    String firstChar = str.substring(0, 1);
    String lastChar = str.substring(str.length() - 1 );
    return (lastChar + str.substring(1, str.length() -1) + firstChar);
    
  }
  return str;
  
}
