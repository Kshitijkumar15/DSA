public class StringRev {
    public static void main(String[] args) {
        String str="kshitij";
        String rev="";
        char c;
        for(int i=0;i<str.length();i++){
            c=str.charAt(i);
            rev=c+rev;
        }
        System.out.println(rev);
    }
}
