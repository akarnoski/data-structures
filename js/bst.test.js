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
    expect(bst.stats['treeDepth']).toBe(1);
});