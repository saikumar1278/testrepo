public class hello {
    public static void main(String[] args) {
        String st = "AB AB";
        String arr[] = st.split("0");
        for (String ele : arr) {
            System.out.println(ele);
        }
    }

}
