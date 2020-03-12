
import java.util.*;
public class fractional_node{
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        LinkedList<Integer> object=new LinkedList<Integer>();
        System.out.println("Enter the Integers in the Linked List (-1 to quit):");
        int n=0,flag=0;
        while(n!=-1){
            n=s.nextInt();
            object.add(n);
        }
        object.pop();
        System.out.println("Enter the integer K:");
        int k=s.nextInt();
        int a=object.size();
        int index=n/k;
        System.out.println("The Fractional Node is "+object.get(index));
    }
}
