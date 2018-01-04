let DoublyLinkedList = require('./dll');

test('Check that one node is head', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    expect(dll.head.data).toBe(3);
});

test('Check that one node is tail', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    expect(dll.tail.data).toBe(3);
});

test('Check that first node becomes tail', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    dll.push(5)
    expect(dll.tail.data).toBe(3);
});

test('Check that second node becomes head', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    dll.push(5)
    expect(dll.head.data).toBe(5);
});

test('Check that size is increased with new nodes', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    dll.push(5)
    expect(dll.size).toBe(2);
});

test('Check that appended node becomes tail', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    dll.push(5)
    dll.append(7)
    expect(dll.tail.data).toBe(7);
});

test('Check that pop returns old head and size is adjusted', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    dll.push(5)
    let popped = dll.pop()
    expect(popped).toBe(5);
    expect(dll.size).toBe(1);
});

test('Check size works', () => {
    let dll = new DoublyLinkedList()
    for(i = 0; i < 10; i++) {
        dll.push(i);
    }
    expect(dll.size).toBe(10);
});

test('Check that shift returns old tail and size is adjusted', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    dll.push(5)
    let shifted = dll.shift()
    expect(shifted).toBe(3);
    expect(dll.size).toBe(1);
});

test('Check that head and tail are changed when one node after shift', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    dll.push(5)
    dll.shift()
    expect(dll.tail.data).toBe(5);
    expect(dll.head.data).toBe(5);
});

test('Check that head and tail are changed when one node after pop', () => {
    let dll = new DoublyLinkedList()
    dll.push(3)
    dll.push(5)
    dll.pop()
    expect(dll.tail.data).toBe(3);
    expect(dll.head.data).toBe(3);
});