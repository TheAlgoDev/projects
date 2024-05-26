//Extends keyword is used when one class inherits from another. Subclass inherits all public and protected fields from parent

// White Potato is part of the nightshade family, does best in cold weather.
public class WhitePotato extends Potato {

    public WhitePotato(String name, double height, double width, int daysGrown, int daysToHarvest) {
        super(name, height, width, daysGrown, daysToHarvest);
    }

// The plants stores extra energy in its roots, creating tubers.
    @Override
    public String storeEnergy() {
        return "White potato has been growing for " + daysGrown + " days now, there are tubers growing underground.";
    }

// Once a critical mass is met and two months passed, the plant begins to propagate through underground shoots.
    @Override
    public String createNewPlant() {
        if (daysGrown > 60)
            return "Potato plant is " + height + " inches tall and " + width + " inches wide, it is creating new plants now.";
        else
            return "Potato plant is too small, it is not creating new plants";
    }

// The age of the potato will determine its harvest date and expected size of tubers.
    @Override
    public String agePotato() {
        String s = super.agePotato();
        return "White" + s;
    }

// Watering the plant results in new growth.
    @Override
    public String waterPotato() {
        String w = super.waterPotato();
        return w + "\nCheck to make sure the soil isn't waterlogged.";
    }
}

