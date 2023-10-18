public class Sum {
    public static void main(String[] args) {
        int array[] ={1,2,3,4};
        int s=0;
        int e=array.length-1;
        int sum=0;
        while(s<=e){
            if(s==e){
                sum+=array[s];
                break;
            }
            sum+=array[s]*10+array[e];
            s++;
            e--;
        }
        System.out.println(sum);
    }
}
