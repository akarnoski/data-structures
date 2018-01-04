let LinkedList = require('./linked_list');

test('Check that one node is head', () => {
    let ll = new LinkedList()
    ll.push(3)
    expect(ll.head.data).toBe(3);
});

test('Check that second node becomes head', () => {
    let ll = new LinkedList()
    ll.push(3)
    ll.push(5)
    expect(ll.head.data).toBe(5);
});

test('Check that size is increased with new nodes', () => {
    let ll = new LinkedList()
    ll.push(3)
    ll.push(5)
    expect(ll.size).toBe(2);
});

test('Test pop returns undefined if no node', () => {
    let ll = new LinkedList()
    expect(ll.pop()).toBe(undefined);
});

test('Check that pop returns value', () => {
    let ll = new LinkedList()
    ll.push(3)
    ll.push(5)
    let popped = ll.pop()
    expect(popped).toBe(5);
});

test('Check that pop adjusts size', () => {
    let ll = new LinkedList()
    ll.push(3)
    ll.push(5)
    ll.pop()
    expect(ll.size).toBe(1);
});

test('Check size works', () => {
    let ll = new LinkedList()
    for(i = 0; i < 10; i++) {
        ll.push(i);
    }
    expect(ll.size).toBe(10);
});

test('Check that search returns node', () => {
    let ll = new LinkedList()
    for(i = 0; i < 10; i++) {
        ll.push(i);
    }
    let searchFor = ll.search(5);
    expect(searchFor.data).toBe(5);
});

test('Check that search returns undefined', () => {
    let ll = new LinkedList()
    for(i = 0; i < 5; i++) {
        ll.push(i);
    }
    let searchFor = ll.search(15);
    expect(searchFor).toBe('Node not in list');
});

test('Check remove decreases size', () => {
    let ll = new LinkedList()
    for(i = 0; i < 5; i++) {
        ll.push(i);
    }
    ll.remove(3)
    expect(ll.size).toBe(4);
});

test('Check removed node is not in list', () => {
    let ll = new LinkedList()
    for(i = 0; i < 5; i++) {
        ll.push(i);
    }
    ll.remove(3)
    expect(ll.search(3)).toBe('Node not in list');
});

test('Check head is updated if old head is removed', () => {
    let ll = new LinkedList()
    ll.push(3)
    ll.push(5)
    ll.remove(5)
    expect(ll.head.data).toBe(3);
});