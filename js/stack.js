let LinkedList = require('./linked_list')

class Stack {
    constructor() {
        this.linked_list = new LinkedList();
    }

    push(data) {
        this.linked_list.push(data);
    }

    pop() {
        let popped = this.linked_list.pop();
        if(popped === undefined) {
            return 'Cannot pop empty stack';
        } else {
            return popped;
        }
    }

    size() {
        return this.linked_list.size;
    }
}

module.exports = Stack;