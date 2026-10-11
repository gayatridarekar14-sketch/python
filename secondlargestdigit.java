public class secondlargestdigit {
    public static void main(String[] args) {
        int n = 985998;
        int largest = -1, second = -1;

        while (n > 0) {
            int d = n % 10;
            n /= 10;

            if (d > largest) {
                second = largest;
                largest = d;
            } else if (d < largest && d > second) {
                second = d;
            }
        }

        if (second == -1)
            System.out.println("Fewer than two distinct digits");
        else
            System.out.println("Second-largest distinct digit: " + second);
    }
}