public class Leap {
    public static void main(String[] args) {
        int year=2000;
        boolean leap=false;
        if(year%4==0){
            if(year%100==0){
                if(year%400==0){
                    leap=true;
                }
                else {
                    leap=false;
                }
            }
            else {
                leap=false;
            }
        }
        else {
            leap=false;
        }
        if(leap){
            System.out.println("leap year");
        }
        else{
            System.out.println("not a leap year");
        }
    }
}
