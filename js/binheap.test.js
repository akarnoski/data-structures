let BinHeap = require('./binheap');

test('Test push for one value', () => {
    let bh = new BinHeap()
    bh.push(3)
    expect(bh.size).toBe(1);
});

test('Test push for five values', () => {
    let bh = new BinHeap()
    for(i = 0; i < 5; i ++) {
        bh.push(i)
    }
    expect(bh.size).toBe(5);
});

test('Test binheap correctly orders values one way', () => {
    let bh = new BinHeap()
    bh.push(3)
    bh.push(5)
    expect(bh.heap_list[0]).toBe(3);
});

test('Test binheap correctly orders values the other way', () => {
    let bh = new BinHeap()
    bh.push(5)
    bh.push(3)
    expect(bh.heap_list[0]).toBe(3);
});

test('Test binheap correctly orders multiple values', () => {
    let bh = new BinHeap()
    bh.push(2)
    bh.push(10)
    bh.push(8)
    bh.push(4)
    bh.push(7)
    expect(bh.heap_list).toEqual([2, 4, 8, 10, 7]);
});

test('Test binheap pop correctly removes value', () => {
    let bh = new BinHeap()
    bh.push(2)
    bh.push(10)
    bh.push(7)
    bh.pop()
    expect(bh.heap_list).toEqual([7, 10]);
});