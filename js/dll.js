class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.previous = null;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    push(data) {
        let newNode = new Node(data);
        if(!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            let oldHead = this.head;
            oldHead.previous = newNode;
            newNode.next = oldHead;
            this.head = newNode;
        }
        this.size += 1;
    }

    append(data) {
        let newTail = new Node(data);
        if(this.tail) {
            let oldTail = this.tail;
            oldTail.next = newTail;
            newTail.previous = oldTail;
            this.tail = newTail
        } else {
            this.head = newTail;
            this.tail = newTail;
        }
    }

    pop() {
        if(self.size === 0) {
            this.head = null
            this.tail = null
        }
        let message = {failure: 'Failure: No nodes available to pop.'}
        if(!this.head) {
            throw new Error(message.failure);
        }
        let returnData = this.head.data;
        if(this.head) {
            this.head = this.head.next;
            this.head.previous = null;
            this.size -= 1;
            if(this.size === 1) {
                this.head = this.tail;
            }
        }
        return returnData;
    }

    shift() {
       if(self.size === 0) {
            this.head = null
            this.tail = null
        }
        let message = {failure: 'Failure: No nodes available to pop.'}
        if(!this.tail) {
            throw new Error('Failure: No nodes available to pop.');
        }
        let returnData = this.tail.data;
        if(this.tail) {
            this.tail = this.tail.previous;
            this.tail.next = null;
            this.size -= 1;
            if(this.size === 1) {
                this.head = this.tail;
            }
        }
        return returnData; 
    }

}

module.exports = DoublyLinkedList;