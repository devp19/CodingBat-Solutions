public int diff21(int n) {
  int result = n - 21;
  
  if(result<0){
    result*=-1;
  }
  
  if(n>21){
    return(2*result);
  }
  
  return(result);
}
