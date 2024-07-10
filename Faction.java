// Factions class is used to represent all the different groups in the Star Wars universe

// Attributes to distinguish name, size of the faction, and how many worlds the group controls
public class Faction {
    private String name;
    private int size;
    private int worldControlled;

    // Constructor
    public Faction(String name, int size, int worldControlled) {
        this.name = name;
        this.size = size;
        this.worldControlled = worldControlled;
    }

    // Getters and Setters
    public void setName(String name) {
        this.name = name;
    }
    public void setSize(int size) {
        this.size = size;
    }
    public void setWorldControlled(int worldControlled) {
        this.worldControlled = worldControlled;
    }

    public String getName() {
        return name;
    }
    public int getSize() {
        return size;
    }
    public int getWorldControlled() {
        return worldControlled;
    }

    // toString Method
    @Override
    public String toString() {
        return "Faction {" +
                "Official name = '" + name + '\'' +
                ", Size of group (1-10)= " + size +
                ", Controls " + worldControlled +
                " worlds in the galaxy. }";
    }
}
