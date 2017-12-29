class Queue {
    constructor() {
        this.queue = []
    }

    enqueue(val) {
        this.queue.push(val)
        this.counter += 1
    }

    dequeue(val) {
        return this.queue.shift();
    }

    peek() {
        return this.queue[0];
    }

    size() {
        return this.queue.length
    }
}

module.exports = Queue;