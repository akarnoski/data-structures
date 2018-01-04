let Deque = require('./deque');

test('Size of Deque is one after appending', () => {
    let d = new Deque()
    d.append(3)
    expect(d.size()).toBe(1);
});

test('Size of Deque is one after appending left', () => {
    let d = new Deque()
    d.appendLeft(3)
    expect(d.size()).toBe(1);
});

test('Size of Deque is two after appending', () => {
    let d = new Deque()
    d.append(3)
    d.append(5)
    expect(d.size()).toBe(2);
});

test('Size of Deque is two after appending and appending left', () => {
    let d = new Deque()
    d.append(3)
    d.appendLeft(5)
    expect(d.size()).toBe(2);
});

test('Size of Deque is two after appending left', () => {
    let d = new Deque()
    d.appendLeft(3)
    d.appendLeft(5)
    expect(d.size()).toBe(2);
});

test('Size of Deque after popping value', () => {
    let d = new Deque()
    d.appendLeft(3)
    d.appendLeft(5)
    d.pop()
    expect(d.size()).toBe(1);
});

test('Pop returns value from back of deque', () => {
    let d = new Deque()
    d.appendLeft(3)
    d.appendLeft(5)
    expect(d.pop()).toBe(3);
});

test('Pop returns value from front of deque', () => {
    let d = new Deque()
    d.appendLeft(3)
    d.appendLeft(5)
    expect(d.popLeft()).toBe(5);
});

test('Size of Deque after popping left', () => {
    let d = new Deque()
    d.appendLeft(3)
    d.appendLeft(5)
    d.popLeft()
    expect(d.size()).toBe(1);
});

test('Peek at value in deque', () => {
    let d = new Deque()
    d.appendLeft(3)
    d.appendLeft(5)
    expect(d.peek()).toBe(3);
});

test('Peek left at value in deque', () => {
    let d = new Deque()
    d.appendLeft(3)
    d.appendLeft(5)
    expect(d.peekLeft()).toBe(5);
});