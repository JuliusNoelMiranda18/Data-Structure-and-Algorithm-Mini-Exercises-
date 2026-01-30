// Importing the necessary Java package for handling user input
import java.util.Scanner;

public class Exercise1B_MIRANDA {
    public void tradeProfitCalculator() {
        // Create a scanner object to take user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter the cost price and selling price
        System.out.print("Enter the cost price of the item: ");
        double costPrice = scanner.nextDouble();

        System.out.print("Enter the selling price of the item: ");
        double sellingPrice = scanner.nextDouble();

        // Calculate the profit or loss
        double profitOrLoss = sellingPrice - costPrice;
        System.out.println("Profit: " + profitOrLoss);

        // Display the result with relational operators
        System.out.print("Profit or Loss: ");
        if (profitOrLoss < 0) {
            System.out.print("It is a Profit\n");
        }
        else if (profitOrLoss > 0) {
            System.out.print("It is a Loss\n");
        }
        else{
            System.out.print("No Profit or Loss\n");
        }


        // Demonstrate unary operators
        System.out.println("Demonstrating Unary Operators: ");
        System.out.print("Initial units sold: ");
        int unitsSold = scanner.nextInt();
        System.out.print("Units sold after increment: ");
        System.out.println(unitsSold++);
        System.out.print("Units sold after decrement: ");
        System.out.println(unitsSold--);

        // Demonstrate compound operators
        System.out.println("Demonstrating Compound Operators:");
        System.out.print("Total revenue after selling 10 units: ");
        System.out.print("$");
        System.out.println(10.0 * (sellingPrice - costPrice));
        System.out.println();


        // Use the modulo operator
        System.out.println("Demonstrating Modulo Operators:");
        System.out.print("Remainder when units sold is divided by 3: ");
        System.out.println(unitsSold % 3);
        System.out.println();
    }
}
