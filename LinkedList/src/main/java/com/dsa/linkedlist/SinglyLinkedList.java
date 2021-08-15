package com.dsa.linkedlist;

public class SinglyLinkedList {

    // properties
    Node head;

    // constructor
    public SinglyLinkedList() {
        this.head = new Node();
    }

    class Node {

        int data;
        Node next;

        public int getData() {
            return data;
        }

        public void setData(int data) {
            this.data = data;
        }

        public Node getNext() {
            return next;
        }

        public void setNext(Node next) {
            this.next = next;
        }

    }

    // methods

    public void addFirst(int element) {

        // create new node
        Node node = new Node();
        // add data to node
        node.setData(element);
        // link previous node to new node
        head.setNext(node);

    }

    public void addLast(int element) {

    }

    public void removeFirst() {

    }

    public void removeLast() {

    }

    public int size() {
        return 0;
    }

    public int get(int index) {
        return 0;
    }

    public void set(int index, int element) {

    }

    public Node getHead() {
        return head;
    }

    public void setHead(Node head) {
        this.head = head;
    }
}
