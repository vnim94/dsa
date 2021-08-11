package com.dsa.dynamicarray;

public class DynamicArray {

    // properties
    private int[] array;
    private int length; // to track size of array

    // constructor
    public DynamicArray() {
        this.array = new int[]{};
        this.length = array.length;
    }

    // methods
    public void add(int value) {

        // create new array with extra length
        int[] newArray = new int[array.length + 1];

        // copy elements from old array to new array
        for (int i = 0; i < array.length; i++) {
            newArray[i] = array[i];
        }

        // add new element
        newArray[array.length] = value;

        // set array as new array
        array = newArray;
        length++;

    }

    public void remove(int index) {

        // create new array with length - 1
        int[] newArray = new int[array.length - 1];

        int removedValue = array[index];

        // copy elements across except removedValue
        for (int i = 0; i < newArray.length; i++) {

            if (array[i] == removedValue) {
                newArray[i] = array[i + 1];
            } else {
                newArray[i] = array[i];
            }

        }

        // set array as new array
        array = newArray;
        length--;

    }

    public int size() {
        return length;
    }

    public int get(int index) {
        return array[index];
    }

    public void set(int index, int value) {
        array[index] = value;
    }

    public boolean contains(int value) {

        for (int i = 0; i < length; i++) {
            if (array[i] == value) {
                return true;
            }
        }

        return false;

    }

    public boolean isEmpty() {

        if (length == 0) {
            return true;
        }

        return false;

    }

    public int indexOf(int value) {

        for (int i = 0; i < length; i ++) {
            if (array[i] == value) {
                return i;
            }
        }

        return -1;

    }

    public void clear() {

        // set array to new empty array
        array = new int[]{};

        // set length to 0
        length = 0;

    }

    // getters and setters
    public int[] getArray() {
        return array;
    }

    public int getLength() {
        return length;
    }

    public void setArray(int[] array) {
        this.array = array;
    }

    public void setLength(int length) {
        this.length = length;
    }
}
