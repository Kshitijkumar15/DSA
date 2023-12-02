public class ReverseNum {
    public static void main(String[] args) {
        int num=56789, r=0;
        while(num>0){
            int rem=num%10;
            r=r*10+rem;
            num=num/10;

        }
        System.out.println(r);
    }
}
