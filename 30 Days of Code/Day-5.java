// https://www.hackerrank.com/challenges/30-loops/problem

import java.util.Scanner;
class Multiples
{
  public static void main(String[] args)
  {
    int n;
    Scanner in = new Scanner(System.in);
      n = in.nextInt();
    int i;
    for ( i=1; i<=10; i++)
    {
      int c;
      c=n*i;
      System.out.println ( n+" x "+i+" = "+c);
    }
  }
}
