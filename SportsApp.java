/*
Brent Thompson
Object Oriented Programming COP 3330C
May 7th, 2024

Main class to demonstrate the creation and use of the sports classes,
Objects are instantiated, details are printed, methods to update values are called, and updated info is printed
 */
public class SportsApp {
   public static void main(String [] args) {
      // Instantiating objects
      Vollyball game1 = new Vollyball("Pumas", 8, true, 0);
      Soccer game2 = new Soccer("Knights", 11, true, "Large");

      // Outputs the details of the sport including details of each sport
      game1.printDetails();
      game2.printDetails();

      // Methods are changing values of the game, such as team size
      game1.addPlayers(2);
      game2.changeTeamsize(8);

      // Prints the new values after being updated
      game1.printDetails();
      game2.printDetails();

      // Expresses gratitude for learning how to write classes
      System.out.println("Thank you Professor for your clear teaching style and enthusiasm");
   }
}

