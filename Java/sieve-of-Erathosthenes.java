import java.util.*;
public class Sieve{
    public static void Erathosthenes(int n){
        boolean prime[]=new boolean[n+1];
        int i;
        for(i=0;i<n;i++){
            prime[i]=true;
        }
        for(int p=2;p*p<=n;p++){
            if(prime[p]==true){
                for(i=p*p;i<=n;i=i+p){
                    prime[i]=false;
                }
            }
        }
        for(i=2;i<=n;i++){
            if(prime[i]==true){
                System.out.println(i);
            }
        }
    }
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the number of prime numbers needed:");
        int n=s.nextInt();
        System.out.println("The Prime Numbers are:");
        Erathosthenes(n);
    }
}
