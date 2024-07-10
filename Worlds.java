// Worlds class is used to represent Worlds in the Star Wars universe

// Attributes to distinguish name, number of moons, and if it has life or not
public class Worlds {
    private String name;
    private int moons;
    private Boolean hasLife;

    // Constructor
    public Worlds(String name, int moons, Boolean hasLife) {
        this.name = name;
        this.moons = moons;
        this.hasLife = hasLife;
    }

    // Getters and Setters
    public void setName(String name) {
        this.name = name;
    }
    public void setMoons(int moons) {
        this.moons = moons;
    }
    public void setHasLife(Boolean False) {
        this.hasLife = False;
    }

    public String getName() {
        return name;
    }
    public int getMoons() {
        return moons;
    }
    public boolean hasLife() {
        return hasLife;
    }

    // toString Method
    @Override
    public String toString() {
        return "Planet information {" +
                "World Name = '" + name + '\'' +
                ", moons orbiting = " + moons +
                ", hasLife = " + hasLife +
                '}';
    }
}
