let BinarySearchTree = require('./bst');

test('Test adding node', () => {
    let bst = new BinarySearchTree()
    bst.insert(3)
    expect(bst.root.data).toBe(3);
});

test('Test adding node', () => {
    let bst = new BinarySearchTree()
    bst.insert(3)
    expect(bst.stats['counter']).toBe(1);
});

test('Test adding node', () => {
    let bst = new BinarySearchTree()
    bst.insert(3)
    bst.insert(5)
    expect(bst.stats['counter']).toBe(2);
});

test('Test adding node', () => {
    let bst = new BinarySearchTree()
    bst.insert(3)
    bst.insert(5)
    expect(bst.root.right.data).toBe(5);
});

test('Test adding node', () => {
    let bst = new BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    expect(bst.root.left.data).toBe(3);
});

test('Test searching nodes', () => {
    let bst = new BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    expect(bst.search(3).data).toBe(3);
});

test('Test searching nodes', () => {
    let bst = new BinarySearchTree()
    expect(bst.search(3)).toBe(undefined);
});

test('Test size of empty tree', () => {
    let bst = new BinarySearchTree()
    expect(bst.stats['counter']).toBe(0);
});

test('Test size', () => {
    let bst = new BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    expect(bst.size()).toBe(3);
});

test('Test size', () => {
    let bst = new BinarySearchTree()
    expect(bst.size()).toBe(0);
});

test('Test depth', () => {
    let bst = new BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    expect(bst.depth()).toBe(1);
});

test('Test depth', () => {
    let bst = new BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    expect(bst.depth()).toBe(1);
});

test('Test depth', () => {
    let bst = new BinarySearchTree()
    expect(bst.depth()).toBe(0);
});

test('Test balance', () => {
    let bst = new BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    expect(bst.balance()).toBe(0);
});

test('Test balance', () => {
    let bst = new BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    expect(bst.balance()).toBe(-1);
});

test('Test balance', () => {
    let bst = new BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    expect(bst.balance()).toBe(1);
});

test('Test contains', () => {
    let bst = new BinarySearchTree()
    for(i = 0; i < 10; i++) {
        bst.insert(i)
    }
    expect(bst.contains(3)).toBe(true);
});

test('Test contains', () => {
    let bst = new BinarySearchTree()
    for(i = 0; i < 5; i++) {
        bst.insert(i)
    }
    expect(bst.contains(8)).toBe(false);
});
