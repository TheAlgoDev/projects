/*
Brent Thompson
Object-Oriented Programming COP 3330C
Professor Ashley Evans
May 25th, 2024

Programming Project 2 Inheritance and Polymorphism
 */


// Potato Farmer contains the growth cycles of a set of potato plants. 5 species are recorded with their plants stats and
// harvest dates calculated. Plants are able to grow tubers and create new plants. Demonstrates Inheritance and Polymorphism

public class PotatoFarmer {
    public static class Main {
        public static void main(String[] args) {
            // Instantiate the child potato objects from parent potato class
            SweetPotato georgia = new SweetPotato("Georgia",3, 2, 5, 120);
            WhitePotato idaho = new WhitePotato("Idaho", 4.5, 3.5, 10, 140);
            SweetPotato ube = new SweetPotato("Ube", 1.3, 1.5, 6, 180);
            WhitePotato russet = new WhitePotato("Russet",6.5, 2.4, 12, 150);
            WhitePotato yukon = new WhitePotato("Yukon",2,3,20,120);

            // Demonstrate polymorphism: Potato references with child class objects
            Potato[] potatoes = {georgia, idaho, ube, russet, yukon};

            // for loop to display and update values for potato crop
            for (Potato potato : potatoes) {
                System.out.println("x---------------------------------------x");
                System.out.println("Here is the current information on " + potato.getName() + ". Please enter new information below.");
                System.out.println(potato.toString());
                System.out.println(potato.createNewPlant());
                System.out.println(potato.storeEnergy());
                System.out.println("Some time has passed since you last updated the crop,\nPlease enter values for each plant below");
                System.out.println(potato.waterPotato());
                System.out.println(potato.agePotato());
            }

            // Printing final information about the potato plants
            System.out.println("Here is the updated information on the plants");
            for (Potato potato : potatoes) {
                System.out.println(potato.getName() + ":");
                System.out.println("Plant height is: " + potato.getHeight() + " inches");
                System.out.println("Plant width is: " + potato.getWidth() + " inches");
                System.out.println("Days since the plant started growing: " + potato.getDaysGrown());
                System.out.println("Days left to harvest: " + potato.getDaysToHarvest());
                System.out.println("x---------------------------------------x");
            }
        }
    }
}
