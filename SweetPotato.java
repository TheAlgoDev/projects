//Extends keyword is used when one class inherits from another. Subclass inherits all public and protected fields from parent

// Sweet potatoes belong to the same family as morning glory, they do best in the heat.
public class SweetPotato extends Potato {

    public SweetPotato(String name, double height, double width, int daysGrown, int daysToHarvest) {
        super(name, height, width, daysGrown, daysToHarvest);
    }

// Potato plant stores extra energy in its roots, growing tubers underground
    @Override
    public String storeEnergy() {
        int numberOfTubers = (daysGrown/2);
        return "Sweet potato has been growing for " + daysGrown + " days now, there are " + numberOfTubers + " tubers growing underground.";
    }

// Sweet potato will send out runnings that root along the surface of the ground, making new plants.
    @Override
    public String createNewPlant() {
        return "Sweet potato is " + height +" inches tall and " + width + " inches wide, it is sending out runners.";
    }

// As the potato gets older, the tubers will grow and multiply
    @Override
    public String agePotato() {
        String s = super.agePotato();
        return "Sweet" + s;
    }

// Watering the plants leads to growth
    @Override
    public String waterPotato() {
        String w = super.waterPotato();
        return "Sweet" + w + "\nThe Sweet Potato is growing fast!";
    }
}
