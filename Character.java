// Character class is used to represent the individual characters in the Star Wars universe

// Attributes to distinguish name, what species the character is a part of, and how powerful they are with the force
public class Character {
    private String name;
    private String species;
    private int powerLevel;

    // Constructor
    public Character(String name, String species, int powerLevel) {
        this.name = name;
        this.species = species;
        this.powerLevel = powerLevel;
    }

    // Getters and Setters
    public void setName(String name) {
        this.name = name;
    }
    public void setSpecies(String species) {
        this.species = species;
    }
    public void setPowerLevel(int powerLevel) {
        this.powerLevel = powerLevel;
    }
    public String getName() {
        return name;
    }
    public String getSpecies() {
        return species;
    }
    public int getPowerLevel() {
        return powerLevel;
    }

    // toString Method
    @Override
    public String toString() {
        return "Character{" +
                "Character name = '" + name + '\'' +
                ", Faction = '" + species + '\'' +
                ", Power Level = " + powerLevel +
                '}';
    }
}
