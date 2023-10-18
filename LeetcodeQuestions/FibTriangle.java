public class FibTriangle {
    public static void main(String[] args) {
        int n1=0,n2=1,n3,n=5,i,j;
        for( i=1;i<=n;i++){
            n1=0;
            n2=1;
            System.out.print(n2+" ");
            for(j=1;j<i;j++){
                n3=n1+n2;
                System.out.print(n +" ");
                n1=n2;
                n2=n3;

            }
            System.out.println(" ");
        }
    }
}
