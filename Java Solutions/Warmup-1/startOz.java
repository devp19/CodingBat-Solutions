public String startOz(String str) {
  
  String result = "";
  
  if (str.length()>0) { 
    if (str.startsWith("oz")){
      return("oz");
    }
    
    else if (str.startsWith("o")){
      return("o");
      
    }
    
    else if (str.substring(1).startsWith("z")){
      return("z");
    }
  
  }
  return(result);
}
