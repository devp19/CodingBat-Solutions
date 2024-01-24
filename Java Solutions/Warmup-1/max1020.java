public int max1020(int a, int b) {
  
  int larger = Math.max(a,b);
  
  if(larger >= 10 && larger <= 20){
    return(larger);
  }
  else if (a>=10 && a<=20){
    return (a);
  }
  else if (b>=10 && b<=20){
    return (b);
  }
  return(0);
  
  
  
}
