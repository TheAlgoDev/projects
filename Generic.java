/*
This class provides a static method which takes an array and one value from the array as arguments, implementing generics

The index of the value provide is returned, and -1 is returned if the value is not found.

 */

public class Generic {
    public static <T> int indexOf(T[] array, T value) {
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals(value)) {
                return i;
            }
        }
        return -1;
    }
}