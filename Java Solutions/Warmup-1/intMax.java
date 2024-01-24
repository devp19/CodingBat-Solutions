public int intMax(int a, int b, int c) {
  
  int firstMax = (int)Math.max(a,b);
  int secondMax = (int)Math.max(b, c);
  
  return((int)Math.max(firstMax, secondMax));
}
