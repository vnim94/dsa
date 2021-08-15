package com.dsa.linkedlist;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SinglyLinkedListTest {

    @Test
    void addFirst() {

        // Arrange
        SinglyLinkedList list = new SinglyLinkedList();

        // Act
        list.addFirst(1);

        // Assert
        assertEquals(1, list.getHead().getNext().getData());

    }

    @Test
    void addLast() {
    }

    @Test
    void removeFirst() {
    }

    @Test
    void removeLast() {
    }

    @Test
    void size() {
    }

    @Test
    void get() {
    }

    @Test
    void set() {
    }
}