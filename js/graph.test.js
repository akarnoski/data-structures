let Graph = require('./graph');

test('Test adding node', () => {
    let g = new Graph()
    g.addNode(3)
    expect(g.getNodes()).toContain(3);
});

test('Test adding multiple nodes', () => {
    let g = new Graph()
    g.addNode(3, 2, 1)
    expect(g.size).toBe(3);
});

test('Test adding same node gets ignored', () => {
    let g = new Graph()
    g.addNode(3, 3)
    expect(g.size).toBe(1);
});

test('Test adding edge', () => {
    let g = new Graph()
    g.addEdge(3, 2)
    expect(g.size).toBe(2);
});

test('Test edges method', () => {
    let g = new Graph()
    for(i = 0; i < 5; i++) {
        g.addEdge(1, i)
    }
    expect(g.edges()).toEqual([1, 0, 1, 1, 1, 2, 1, 3, 1, 4]);
});

test('Test edges returns none', () => {
    let g = new Graph()
    expect(g.edges()).toBe('No edges in graph');
});

test('Test edge gets ignored if already in graph', () => {
    let g = new Graph()
    g.addEdge(3, 2)
    g.addEdge(3, 2)
    expect(g.size).toBe(2);
});

test('Test deleting node', () => {
    let g = new Graph()
    g.addNode(3, 4, 6, 2, 5)
    g.delNode(4)
    expect(g.getNodes()).not.toContain(4);
});

test('Test deleting only value', () => {
    let g = new Graph()
    g.addNode(3)
    g.delNode(3)
    expect(g.getNodes()).not.toContain(4);
});

test('Test error from deleting node not in graph', () => {
    let g = new Graph()
    expect(g.delNode()).toBe('No such node');
});

test('Test true has node method', () => {
    let g = new Graph()
    g.addNode(3)
    expect(g.hasNode(3)).toBeTruthy();
});

test('Test false has node method', () => {
    let g = new Graph()
    g.addNode(5)
    expect(g.hasNode(3)).toBeFalsy();
});

test('Test neighbors', () => {
    let g = new Graph()
    g.addEdge(3, 2)
    expect(g.neighbors(3)).toEqual([2]);
});

test('Test neighbors when no node is in graph', () => {
    let g = new Graph()
    expect(g.neighbors(3)).toBe('No such node');
});

test('Test adjacent for two values with edge', () => {
    let g = new Graph()
    g.addEdge(1, 2)
    expect(g.adjacent(1, 2)).toBeTruthy();
});

test('Test adjacent for two values without edge', () => {
    let g = new Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    expect(g.adjacent(3, 2)).toBeFalsy();
});

test('Test adjacent without value in graph', () => {
    let g = new Graph()
    g.addEdge(1, 2)
    expect(g.adjacent(1, 3)).toBe('Both nodes not in graph');
});

test('Test adjacent with no values in graph', () => {
    let g = new Graph()
    expect(g.adjacent(1, 3)).toBe('Both nodes not in graph');
});

test('Test delete edge of two values', () => {
    let g = new Graph()
    g.addEdge(1, 2)
    g.delEdge(1, 2)
    expect(g.adjacent(1, 2)).toBeFalsy();
});

test('Test delete on values not in graph', () => {
    let g = new Graph()
    expect(g.delEdge(1, 2)).toBe('Edge not in graph');
});