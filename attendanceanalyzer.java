import java.util.Scanner;

public class attendanceanalyzer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter total working days: ");
        int totalDays = sc.nextInt();

        System.out.print("Enter present days: ");
        int presentDays = sc.nextInt();

        int absentDays = totalDays - presentDays;
        double percentage = (presentDays * 100.0) / totalDays;

        System.out.println("Absent days: " + absentDays);
        System.out.println("Attendance percentage: " + percentage + "%");

        if (percentage >= 75) {
            System.out.println("Eligible for bonus");
        } else {
            System.out.println("Not eligible for bonus");
        }

        sc.close();
    }
}
