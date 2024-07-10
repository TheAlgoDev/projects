/*
Brent Thompson
COP 3330C 31953 Object-Oriented Programming
Professor Ashley Evans
June 26th 2024

Programming Project 6 : Generics Part Two

This class is demonstrating the use of generics by first creating a series of objects to then fill three different
instances of generic data structure's with.

First the information is printed to display initial state, second are the static
methods that are called to changed different types of data within the structure.
 */

public class GenericsDemoApp {
    public static void main(String[] args) {


        // Instantiate several objects
        Worlds hoth = new Worlds("Hoth", 2, Boolean.TRUE);
        Worlds corusant = new Worlds("Corusant", 0, Boolean.TRUE);
        Worlds tatooine = new Worlds("Tatooine", 3, Boolean.TRUE);

        Character luke = new Character("Luke Skywalker", "human", 7);
        Character obiwan = new Character("Obi-Wan Kenobi", "human", 6);
        Character c3po = new Character("C3PO", "android", 1);
        Character yoda = new Character("Yoda", "unknown", 9);

        Faction republic = new Faction("Republic", 5, 9000);
        Faction empire = new Faction("Empire", 7, 12000);
        Faction hutts = new Faction("Hutt Space", 1, 3);

        genericDataContainer<Worlds> worldsContainer = new genericDataContainer<>();


        // Use the genericContainer to interact with the objects
        worldsContainer.addItem(hoth);
        worldsContainer.addItem(corusant);
        worldsContainer.addItem(tatooine);
        System.out.println("Worlds of the Star Wars Universe...\n" +
                ".....\n" +
                ".....\n\n" +
                ".....\n\n");
        worldsContainer.printList();


        genericDataContainer <Character> charactersContainer = new genericDataContainer<>();
        charactersContainer.addItem(luke);
        charactersContainer.addItem(obiwan);
        charactersContainer.addItem(c3po);
        charactersContainer.addItem(yoda);
        System.out.println("Characters of Episode Four: A New Hope...\n" +
                ".....\n" +
                ".....\n\n" +
                ".....\n\n");
        charactersContainer.printList();


        genericDataContainer <Faction> factionsContainer = new genericDataContainer<>();
        factionsContainer.addItem(republic);
        factionsContainer.addItem(empire);
        factionsContainer.addItem(hutts);
        System.out.println("Factions of Star Wars: A New Hope...\n" +
                ".....\n" +
                ".....\n\n" +
                ".....\n\n");
        factionsContainer.printList();

        // Perform methods are various data types.
        hutts.setName("Jabba's Kingdom "); // Jabba dies and is replaced
        yoda.setName("Yoda the Old"); // Yoda gets older and less powerful
        yoda.setPowerLevel(4);
        luke.setPowerLevel(9); // Luke begins to grow in strength
        hoth.setHasLife(Boolean.FALSE); // Hoth is attacked and glassed
        republic.setName("Old Republic");
        empire.setName("Imperial Empire");
        System.out.println("\n\n\n\nEvents of Episode Four play out..." +
                "Some information has changed, here is the final state of the galaxy..." +
                "...\n\n\n\n");


        // Final print to show updated values.
        System.out.println("\n\nWorlds: \n");
        worldsContainer.printList();
        System.out.println("\n\nCharacters: \n");
        charactersContainer.printList();
        System.out.println("\n\nFactions: \n");
        factionsContainer.printList();





    }
}



