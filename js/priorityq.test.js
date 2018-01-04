let PriorityQueue= require('./priorityq');

test('Test inserting value using max to check', () => {
    let p = new PriorityQueue()
    p.insert('okay', 1)
    expect(p.max).toBe(1);
});

test('Test inserting multiple values using max to check', () => {
    let p = new PriorityQueue()
    for(i = 0; i < 10; i ++) {
        p.insert('okay', i)
    }
    expect(p.max).toBe(9);
});

test('Test popping highest priority', () => {
    let p = new PriorityQueue()
    for(i = 0; i < 10; i ++) {
        p.insert('inserted: ' + i, i)
    }
    expect(p.pop()).toBe('inserted: 9');
});

test('Test popping first value inserted at same priority', () => {
    let p = new PriorityQueue()
    for(i = 0; i < 5; i ++) {
        p.insert('inserted: ' + i, 3)
    }
    expect(p.pop()).toBe('inserted: 0');
});

test('Test pop from empty priority', () => {
    let p = new PriorityQueue()
    expect(p.pop()).toBe('Nothing to pop');
});

test('Test popping twice returns in correct order', () => {
    let p = new PriorityQueue()
    p.insert('this is priority 5', 5)
    p.insert('this is priority 7', 7)
    p.pop()
    expect(p.pop()).toBe('this is priority 5');
});

test('Test peek to look at highest priority', () => {
    let p = new PriorityQueue()
    for(i = 0; i < 10; i ++) {
        p.insert('inserted: ' + i, i)
    }
    expect(p.peek()).toBe('inserted: 9');
});

test('Test peek to look first value at highest priority', () => {
    let p = new PriorityQueue()
    for(i = 0; i < 10; i ++) {
        p.insert('inserted: ' + i, 7)
    }
    expect(p.peek()).toBe('inserted: 0');
});

test('Test helped function actaully works', () => {
    let p = new PriorityQueue()
    for(i = 0; i < 5; i ++) {
        p.insert('inserted: ' + i, i)
    }
    expect(p.max).toBe(4);
    p.pop()
    expect(p.max).toBe(3);
});