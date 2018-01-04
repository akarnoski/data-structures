let DoublyLinkedList = require('./dll')

class Deque {
    constructor() {
        this.dll = new DoublyLinkedList();
    }

    append(data) {
        this.dll.append(data);
    }

    appendLeft(data) {
        this.dll.push(data);
    }

    pop() {
        try {
            return this.dll.shift();
        } catch(e) {
            return 'Nothing to pop'
        }
    }

    popLeft() {
        try {
            return this.dll.pop();
        } catch(e) {
            return 'Nothing to pop'
        }
    }

    peek() {
        if(this.dll.size === 0) {
            return undefined;
        }
        return this.dll.tail.data;
    }

    peekLeft() {
        if(this.dll.size === 0) {
            return undefined;
        }
        return this.dll.head.data;
    }

    size() {
        return this.dll.size;
    }
}

module.exports = Deque;