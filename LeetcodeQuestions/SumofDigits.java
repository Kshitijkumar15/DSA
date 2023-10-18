public class SumofDigits {
    static  int Getsum(int n){
        int sum=0;
        while(n!=0){
            sum=sum+n%10;
            n=n/10;
        }

        return sum;
    }

    public static void main(String[] args) {
        int n=777;
        System.out.println(Getsum(n));
    }
}
