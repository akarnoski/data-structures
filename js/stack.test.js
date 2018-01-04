let Stack = require('./stack');

test('Test pushing one value', () => {
    let s = new Stack()
    s.push(3)
    expect(s.size()).toBe(1);
});

test('Test pushing a bunch of values value', () => {
    let s = new Stack()
    for(i = 0; i < 10; i ++) {
        s.push(i)
    }
    expect(s.size()).toBe(10);
});

test('Test pushing a bunch of values value and popping some', () => {
    let s = new Stack()
    for(i = 0; i < 10; i ++) {
        s.push(i)
    }
    for(i = 0; i < 3; i ++) {
        s.pop()
    }
    expect(s.size()).toBe(7);
});

test('Test pop returns value', () => {
    let s = new Stack()
    s.push(3)
    expect(s.pop()).toBe(3);
});

test('Test pop returns error if no values', () => {
    let s = new Stack()
    expect(s.pop()).toBe('Cannot pop empty stack');
});