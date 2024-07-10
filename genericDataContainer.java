/*
This genericDataContainer class is a demonstration of a Generic collection, that can take an array of any type, and search
that array for the index of an item contained within. Provides methods to be used on DataContainer.
 */


import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class genericDataContainer<T> {
    private List<T> items;

    public genericDataContainer() {
        items = new ArrayList<>();
    }
    public void addItem(T item) {
        items.add(item);
    }
    public void removeItem(T item) {
        items.remove(item);
    }
    public T retrieveItem(int index) {
        return items.get(index);
    }
    public int getListSize(List<T> items) {
        return items.size();
    }
    public void sortList(List<T> items) {
        Stream<T> sorted = items.stream().sorted();
    }
    public void printList() {
        for (T item : items) {
            System.out.println(item);
        }
    }


}
