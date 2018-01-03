let DoublyLinkedList = require('./dll')

class Queue {
    constructor() {
        this.dll = new DoublyLinkedList();
    }

    enqueue(val) {
        this.dll.push(val)
    }

    dequeue(val) {
        return this.dll.shift();
    }

    peek() {
        if(this.dll.size === 0) {
            return undefined
        }
        return this.dll.tail.data;
    }

    size() {
        return this.dll.size
    }
}

module.exports = Queue;