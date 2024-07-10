/*
Brent Thompson
COP 3330C 31953 Object-Oriented Programming
Professor Ashley Evans
June 26th 2024

Programming Project 6 : Generics Part One

This class is demonstrating the use of generics to contain arrays to search through.

The Generic class is able to accept an array of any kind as well as a search term.
The single indexOf method uses these two parameters, of any type, to preform a static method.

The only user inputs are for a search term in each array, the outputs are simple print messages depending on outcome.

 */
import java.util.Scanner;

public class GenericArrayDemo {
    public static void main(String[] args) {

        // Display the use of Generic method on three different data types
        Integer[] intArray = {0,1,2,3,4,5,6,7,8,9};
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number to search in the array: ");
        int checkIndex = sc.nextInt();
        int FirstIndex = Generic.indexOf(intArray, checkIndex);
        if (FirstIndex >= 0) {
            System.out.println(checkIndex + " is at position "+  FirstIndex);
        } else {
            System.out.println("The integer " + checkIndex + " is not in this array. ");
        }

        // String Example
        String[] strArray = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        Scanner sc2 = new Scanner(System.in);
        System.out.println("Enter the word for a number to search for in the array: ");
        String searchWord = sc2.nextLine();
        int secondIndex = Generic.indexOf(strArray, searchWord);
        if (secondIndex >= 0) {
            System.out.println(searchWord + " is at position "+  secondIndex);
        } else {
            System.out.println("The word " + searchWord + " is not found in the array");

        }

        // Float Example
        Float[] fltArray  = {.0F, .1F, .2F, .3F, .4F, .5F, .6F, .7F, .8F, .9F};
        Scanner sc3 = new Scanner(System.in);
        System.out.println("Enter a float between 0 and 1 to search for in the array: ");
        float searchFloat = sc3.nextFloat();
        int thirdIndex = Generic.indexOf(fltArray, searchFloat);
        if (thirdIndex >= 0) {
            System.out.println(searchFloat + " is at position "+ thirdIndex);
        } else {
            System.out.println("The float " + searchFloat + " is not in this array. " );
        }
    }
}
