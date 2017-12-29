let Queue = require('./que_');

test('Size of Queue is one after enqueue', () => {
    let q = new Queue()
    q.enqueue(3)
    expect(q.size()).toBe(1);
});

test('Size of Queue is updated after enqueue', () => {
    let q = new Queue()
    q.enqueue(3)
    q.enqueue(5)
    expect(q.size()).toBe(2);
});

test('Peek returns value in queue', () => {
    let q = new Queue()
    q.enqueue(3)
    expect(q.peek()).toBe(3);
});

test('Peek returns next value to be dequeued', () => {
    let q = new Queue()
    q.enqueue(3)
    q.enqueue(5)
    expect(q.peek()).toBe(3);
});

test('Remove value after enqueue', () => {
    let q = new Queue()
    q.enqueue(3)
    var removed = q.dequeue()
    expect(removed).toBe(3);
});

test('Remove first value enqued', () => {
    let q = new Queue()
    q.enqueue(3)
    q.enqueue(5)
    var removed = q.dequeue()
    expect(removed).toBe(3);
});

test('Return undefined if no values in queue', () => {
    let q = new Queue()
    var removed = q.dequeue()
    expect(removed).toBe(undefined);
});

test('Value is removed and new size is reflected', () => {
    let q = new Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.dequeue()
    expect(q.size()).toBe(1);
});