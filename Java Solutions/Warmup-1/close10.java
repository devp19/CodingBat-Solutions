public int close10(int a, int b) {
  int diffA = Math.abs(a-10);
  int diffB = Math.abs(b-10);
  
  if(diffA > diffB){
    return(b);
  }
  else if(diffB > diffA){
    return(a);
  }
  return(0);
}
