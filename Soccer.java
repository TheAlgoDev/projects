/*
Soccer Class
Represents the sport of soccer. Soccor has a team name, a team size, a field size, and is either ranked or unranked.
 */

public class Soccer {
    // Attributes

    private String teamname;

    private int teamsize;

    private boolean isRanked;

    private String fieldsize;

    // Constructor

    public Soccer (String teamname, int teamsize, boolean isRanked, String fieldsize){
        this.teamname = teamname;
        this.teamsize = teamsize;
        this.isRanked = isRanked;
        this.fieldsize = fieldsize;

    }
    // Overloaded Constructor

    public Soccer (){
        this.teamname = null;
        this.teamsize = 0;
        this.isRanked = false;
        this.fieldsize = null;
    }
    // Getters and Setters

    public String getTeamname(){
        return teamname;
    }
    public void setTeamname(String teamname){
        this.teamname = teamname;
    }
    public int getTeamsize(){
        return teamsize;
    }
    public void setTeamsize(int teamsize){
        this.teamsize = teamsize;
    }
    public boolean getIsRanked() {
        return isRanked;
    }
    public void setIsRanked(boolean isRanked) {
        this.isRanked = isRanked;
    }
    public String getFieldsize() {
        return fieldsize;
    }
    public void setFieldsize(String fieldsize) {
        this.fieldsize = fieldsize;
    }
    // Custom method, changes the team size
    public void changeTeamsize(int teamsize){
        System.out.println("Team size changed to: " + teamsize);
        this.teamsize = teamsize;
    }
    // Print Method
    public void printDetails(){
        System.out.println("Teamname: " + teamname + "\nSize of team: " + teamsize + "\nThis is a ranked match: " + isRanked + "\nThe size of the field is: " + fieldsize);
    }
}
