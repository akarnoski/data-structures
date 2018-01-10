class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
        this.parent = null;
        this.depth = 0;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
        this.stats = {
            'counter': 0,
            'treeDepth': 0,
            'leftDepth': 0,
            'rightDepth': 0,
        }
    }

    insert(data) {
        let newNode = new Node(data);
        if(!this.root) {
            this.root = newNode;
            this.stats['counter'] += 1
            return
        }
        let curr = this.root;
        while(curr) {
            if(newNode.data > curr.data) {
                if(curr.right === null) {
                    newNode.depth += 1;
                    this.adjustStats(newNode);
                    newNode.parent = curr;
                    curr.right = newNode;
                    break;
                }
                newNode.depth += 1;
                curr = curr.right;
            }
            if(newNode.data < curr.data) {
                if(curr.left === null) {
                    newNode.depth += 1;
                    this.adjustStats(newNode);
                    newNode.parent = curr;
                    curr.left = newNode;
                    break
                }
                newNode.depth += 1;
                curr = curr.left;
            }
        }
    }

    search(data) {
        try {
            let curr = this.root;
            while(curr) {
                if(curr.data === data) {
                    return curr;
                }
                if(curr.data < data) {
                    if(curr.right === null) {
                        return;
                    }
                    curr = curr.right;
                }
                if(curr.data > data) {
                    if(curr.left === null) {
                        return;
                    }
                    curr = curr.left;
                }
            }
        } catch(e) {
            return 'No nodes to search'
        }
    }

    depth() {
        return this.stats['treeDepth'];
    }

    size() {
        return this.stats['counter'];
    }

    contains(data) {
        if(this.search(data) !== undefined) {
            return true;
        } else {
            return false;
        }
    }

    balance() {
        return this.stats['leftDepth'] - this.stats['rightDepth'];
    }

    
    adjustStats(node) {
        this.stats['counter'] += 1;
        let currentDepth = this.stats['treeDepth'];
        let newDepth = node.depth;
        if(newDepth > currentDepth) {
            this.stats['treeDepth'] = newDepth;
        }
        if(node.data < this.root.data) {
            if(newDepth > this.stats['leftDepth']) {
                this.stats['leftDepth'] = newDepth;
            }
        }
        if(node.data > this.root.data) {
            if(newDepth > this.stats['rightDepth']) {
                this.stats['rightDepth'] = newDepth;
            }
        }
    }
}

module.exports = BinarySearchTree;