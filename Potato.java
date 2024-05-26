// The implements keyword is used when a class wants to implement and interface.
import java.util.Scanner; // I could not figure out how to accept input without the package.
// Scanner allows for user input

public abstract class Potato implements rootVegetable {

    // Protected is an access modifier used for field. methods, and constructors
    protected String name;
    protected double height;
    protected double width;
    protected int daysGrown;
    protected int daysToHarvest;

    // Constructor
    public Potato(String name, double height, double width, int daysGrown, int daysToHarvest) {
        this.name = name;
        this.height = height;
        this.width = width;
        this.daysGrown = daysGrown;
        this.daysToHarvest = daysToHarvest;

    }

    /* Setters */
    public void setName(String name) {
        this.name = name;
    }

    public void setHeight(float height) {
        this.height = height;
    }

    public void setWidth(float width) {
        this.width = width;
    }

    public void setDaysGrown(int daysGrown) {
        this.daysGrown = daysGrown;
    }

    public void setDaysToHarvest(int daysToHarvest) {
        this.daysToHarvest = daysToHarvest;
    }
    /* Getters */

    public String getName() {
        return name;
    }

    public double getHeight() {
        return height;
    }

    public double getWidth() {
        return width;
    }

    public int getDaysGrown() {
        return daysGrown;
    }

    public int getDaysToHarvest() {
        return daysToHarvest;
    }


    // First method ages the potato to its harvest time, input is days grown
    public String agePotato(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the number of days the potato has been growing...");
        int userInput = scanner.nextInt();
        this.daysGrown = userInput;
        this.daysToHarvest -= userInput;
        System.out.println(name + " aged by " + daysGrown + " days. Keep an eye on it!");
        return "potato has " + daysToHarvest + " days left until harvest";
    }

    // Second method records growth with input of rainfall in inches

    public String waterPotato(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("How many inches of rain has the plant received?");
        int userInput = scanner.nextInt();
        float inchesOfRain = userInput;
        this.height += (float) (2.5 * inchesOfRain); // 2.5 is a growth constant for this plant
        this.width += (float) (1.5 * inchesOfRain);  // 1.5 is a growth constant for this plant
        System.out.println(name + " received " + inchesOfRain + " inches of rain!");
        return "After " + inchesOfRain + " inches of rain, " + "The plant is now\n" +
                height + " inches tall and " + width + " inches wide. Wow!";
    }

    @Override
    public String toString(){
        return "Potato plant is " + height + " Tall and ready to harvest in " + daysToHarvest + " days.";
    }
}
