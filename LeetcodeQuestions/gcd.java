public class gcd {
    public static void main(String[] args) {
        int n1=50,n2=60;
        while(n1!=n2){
            if(n1>n2) {
                n1 = n1 - n2;
            }
            else{
                n2=n2-n1;
            }
            }
        System.out.println(n2);

    }
}
