package com.dsa.dynamicarray;

import org.junit.jupiter.api.*;
import org.junit.jupiter.api.io.TempDir;

import static org.junit.jupiter.api.Assertions.*;

class DynamicArrayTest {

    private DynamicArray dArr;

    @BeforeEach
    void setup() {
        dArr = new DynamicArray();
    }

    @Test
    @DisplayName("new initialised dynamicArray has length of 0 and no elements")
    void new_dynamicArray() {

        // Arrange

        // Act

        // Assert
        assertEquals(0, dArr.getLength());

    }

    @Test
    @DisplayName("adding to a new dynamicArray returns length of 1 and zero-index element equal to added value")
    void add_to_new_dynamicArray() {

        // Arrange

        // Act
        dArr.add(1);

        // Assert
        assertEquals(1, dArr.getLength());
        assertEquals(1, dArr.getArray()[0]);

    }

    @Test
    @DisplayName("adding to an existing dynamicArray")
    void add_to_existing_dynamicArray() {

        // Arrange

        // Act
        dArr.add(1);
        dArr.add(2);
        dArr.add(3);

        // Assert
        assertEquals(3, dArr.getArray().length);
        assertEquals(1, dArr.getArray()[0]);
        assertEquals(2, dArr.getArray()[1]);
        assertEquals(3, dArr.getArray()[2]);

    }

    @Test
    @DisplayName("remove() method removes element at specified index and reduces length of the dynamicArray")
    void remove() {

        // Arrange
        int[] arr = {1,2,3};
        dArr.setArray(arr);
        dArr.setLength(arr.length);

        // Act
        dArr.remove(1);

        // Assert
        assertEquals(2, dArr.getLength());
        assertEquals(1, dArr.getArray()[0]);
        assertEquals(3, dArr.getArray()[1]);

    }

    @Test
    @DisplayName("size() method returns length of 0 for new, empty dynamicArray")
    void size() {

        // Arrange
        dArr.setLength(2);

        // Act
        int size = dArr.size();

        // Assert
        assertEquals(2, size);

    }

    @Test
    @DisplayName("get() method returns value of element at the index in the array")
    void get() {

        // Arrange
        int[] arr = {1,2,3};
        dArr.setArray(arr);
        dArr.setLength(arr.length);

        // Act
        int element = dArr.get(2);

        // Assert
        assertEquals(3, element);

    }

    @Test
    @DisplayName("set() method sets the value at the index in the array")
    void set() {

        // Arrange
        int[] arr = {1,2,3};
        dArr.setArray(arr);
        dArr.setLength(arr.length);

        // Act
        dArr.set(2, 5);

        // Assert
        assertEquals(5, dArr.getArray()[2]);

    }

    @Test
    @DisplayName("contains() method returns true if specified value is in the array")
    void contains() {

        // Arrange
        int[] arr = {1,2,3};
        dArr.setArray(arr);
        dArr.setLength(arr.length);

        // Act
        boolean result = dArr.contains(3);

        // Assert
        assertTrue(result);

    }

    @Test
    @DisplayName("contains() method returns false if specified value not in array")
    void does_not_contain() {

        // Arrange

        // Act
        boolean result = dArr.contains(1);

        // Assert
        assertFalse(result);

    }

    @Test
    @DisplayName("isEmpty() method returns true if array has not elements")
    void isEmpty() {

        // Arrange

        // Act
        boolean result = dArr.isEmpty();

        // Assert
        assertTrue(result);

    }

    @Test
    @DisplayName("isEmpty() method returns false if array has elements")
    void isNotEmpty() {

        // Arrange
        int[] arr = {1,2,3};
        dArr.setArray(arr);
        dArr.setLength(arr.length);

        // Act
        boolean result = dArr.isEmpty();

        // Assert
        assertFalse(result);

    }

    @Test
    @DisplayName("indexOf() method returns index of element if present in array")
    void indexOf() {

        // Arrange
        int[] arr = {1,2,3};
        dArr.setArray(arr);
        dArr.setLength(arr.length);

        // Act
        int index = dArr.indexOf(3);

        // Assert
        assertEquals(2, index);

    }

    @Test
    @DisplayName("indexOf() method returns -1 if element not present in array")
    void indexOfNonExistentElement() {

        // Arrange

        // Act
        int index = dArr.indexOf(2);

        // Assert
        assertEquals(-1, index);

    }

    @Test
    @DisplayName("clear() method empties the array")
    void clear() {

        // Arrange
        int[] arr = {1,2,3};
        dArr.setArray(arr);
        dArr.setLength(arr.length);

        // Act
        dArr.clear();

        // Assert
        assertEquals(0, dArr.getLength());

    }

}





















