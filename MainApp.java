/*
Brent Thompson
COP 3330C 31953 Object-Oriented Programming
Professor Ashley Evans
June 13th 2024

Programming Project 5 - Collections

This MainApp will create a collection of entries, and showcase features from the Collection Framework
 */

/*
The difference between a collection and the collections framework is that a collection is one sing kind data that
holds multiple points of data, while collections is the larger framework within Java that contains the code
for many different types of data structures and their methods.

The biggest difference between a class and an interface is that the class is the thing that is being worked with while
an interface is the system that determines what the things can do. An interface will allow a class to inherit specific
attributes and methods, to be used in programming.

 */
import java.util.*;


public class MainApp {
    public static void main(String[] args) {
        // Start scanner object for entries
        Scanner scanner = new Scanner(System.in);

        // Create a List from user inputs
        System.out.println("Enter eight words to be added to list.\n");
        List<String> list = getEntries(scanner);

        // Print the List using an enhanced for loop
        System.out.println("All eight entries: (as type..." + list.getClass().getSimpleName() + ")");
        for (String entry : list) {
            System.out.println(entry);
        }
        // Sort the List using basic sort method, by alphabetical with capitals listed first
        System.out.println("Sorted entries by alphabetical order: ");
        Collections.sort(list);
        System.out.println(list);

        // Custom Sort the List by entry character length
        System.out.println("Sorted entries by length of entry: ");
        Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return Integer.compare(o2.length(), o1.length());
            }});
        System.out.println(list);

        // Shuffle the list using shuffle method
        System.out.println("Shuffled words: ");
        Collections.shuffle(list);
        System.out.println(list + list.getClass().getSimpleName());

        // Search the List with a word provide by user
        System.out.println("Search for a word: \n");
        String targetWord = scanner.nextLine();
        search(list, targetWord);

        // Reverse the order of the list
        System.out.println("Reversing the order of the list: ");
        Collections.reverse(list);
        System.out.println(list);
        // Swap the first and the second entries in the list
        System.out.println("Swapping the entries in position one and two");
        Collections.swap(list, 0, 1);
        System.out.println(list);

        // Convert the List to an array
        System.out.println("Converting list to an array: ");
        String[] listArray = list.toArray(new String[0]);
        for (String arrayWord : listArray) {
            System.out.println(arrayWord);
        }

        // Covert the array back to a list
        System.out.println("Converting the array back to a list: ");
        ArrayList<String> newList = new ArrayList<>(Arrays.asList(listArray));
        System.out.println(newList + " as type: " + newList.getClass().getSimpleName());

    }
    // Method creates the list by iterating through 8 entries
    public static ArrayList<String> getEntries(Scanner scanner) {
        ArrayList<String> list = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            System.out.print("Enter entry " + (i + 1) + ": ");
            String entry = scanner.nextLine();
            // Check to make sure entry is not already in list
            if (!list.contains(entry)) {
                list.add(entry);
            } else {
                System.out.println(entry + " is already in the list, please try again.");
                i--;
            }
        }
        System.out.println("\nThank you for providing these entries...");
        return list;
    }
    // Method searches the list with a target word, returns index or not found message
    public static void search(List<String> list, String targetWord) {
        int index = list.indexOf(targetWord);
        if (index == -1) {
            System.out.println(targetWord + " not found in the list");
        } else {
            System.out.println(targetWord + " found at index " + index);
        }
        System.out.println("Search complete \n");
    }

}
