public class Palliondrome {
    public static void main(String[] args) {
        int n=2222;
        int sum=0;
        int r,temp;
        temp=n;
        while(n>0){
            r=n%10;
            sum=(sum*10)+r;
            n=n/10;
        }
        if(temp==sum){
            System.out.println("Palliondrome");
        }
        else {
            System.out.println("not");
        }
    }
}
