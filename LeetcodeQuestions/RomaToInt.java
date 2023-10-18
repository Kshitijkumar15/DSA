import java.util.HashMap;

public class RomaToInt {
    public static void romantoInt(String s){
        HashMap<Character,Integer>mp=new HashMap<Character,Integer>();
        mp.put('I',1);
        mp.put('L',3);
        s=s.replace("IV","IIII");
        int num=0;
        for(int i=0;i<s.length();i++){
            num=num+(mp.get(s.charAt(i)));
        }
        System.out.println(num);

    }

    public static void main(String[] args) {
        romantoInt("ILIV");
    }
}
