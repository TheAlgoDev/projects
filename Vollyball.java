/*
 Vollyball class
 Represents the sport of vollyball. Vollyball has a team, number of players, a court type, and points
*/

public class Vollyball {
    // Attributes

    private String teamname;

    private int players;

    private boolean onSand;

    private int points;

    // Constructor

    public Vollyball (String teamname, int players, boolean onSand, int points){
        this.teamname = teamname;
        this.players = players;
        this.onSand = onSand;
        this.points = points;

    }
    // Overloaded Constructor

    public Vollyball(){
        this.teamname = null;
        this.players = 0;
        this.onSand = false;
        this.points = 0;
    }
    // Getters and Setters

    public String getTeamname(){
        return teamname;
    }
    public void setTeamname(String teamname){
        this.teamname = teamname;
    }
    public int getPlayers(){
        return players;
    }
    public void setPlayers(int players){
        this.players = players;
    }
    public boolean getOnSand(){
        return onSand;
    }
    public void setOnSand(boolean onSand){
        this.onSand = onSand;
    }
    public int getPoints(){
        return points;
    }
    public void setPoints(int points){
        this.points = points;
    }

    // Custom method, adds a number of players to the total
    public void addPlayers(int players){
        System.out.println(players + "Players added to team, resume game");
        this.players += players;
    }
    // Print Method, displays all the relevant data
    public void printDetails(){
        System.out.println("Teamname: " + teamname + "\nNumber of players: " + players + "\nThe court is sand: " + onSand + "\nTotal points: " + points);
    }
}

