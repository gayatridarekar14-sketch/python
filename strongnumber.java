import java.util.Scanner;

public class strongnumber {

    // Returns factorial of a digit (0-9)
    static int factorial(int n) {
        int fact = 1;
        for (int i = 2; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Number: ");
        int num = sc.nextInt();

        int temp = num;
        int sum = 0;

        while (temp > 0) {
            int digit = temp % 10;      // extract last digit
            sum += factorial(digit);    // add its factorial
            temp /= 10;                 // remove last digit
        }

        if (sum == num) {
            System.out.println(num + " is a Strong Number.");
        } else {
            System.out.println(num + " is not a Strong Number.");
        }
    }
}