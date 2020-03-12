
// Java Program to find a Modular Node from the end which is the first element from the end which is divisible by a number given by User

import java.util.*; 
public class modular_node{
    public static void main(String[] args){
        Scanner S=new Scanner(System.in);
        LinkedList<Integer> object=new LinkedList<Integer>();
        System.out.println("Enter the Integers in the Linked List (-1 to quit):");
        int n=0,flag=0;
        while(n!=-1){
            n=S.nextInt();
            object.add(n);
        }
        System.out.println("Enter the Integer K:");
        int k=S.nextInt();
        while(object.size()>0){
            int a=object.pop();
            if(a%k==0){
                System.out.println("The Node is at the position:"+object.size());
                flag=1;
                break;
            }
        }
        if(flag==0){
            System.out.println("Element not found");
        }
    }
}
