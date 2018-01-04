class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    push(data) {
        let newNode = new Node(data);
        if(this.head) {
            newNode.next = this.head;
        }
        this.head = newNode;
        this.size += 1;
    }

    pop() {
        if(!this.head) {
            return undefined;
        }
        let returnData = this.head.data;
        this.head = this.head.next;
        this.size -= 1;
        return returnData;
    }

    search(data) {
        let searching = this.head;
        try {
            while(this.head) {
                if(data === searching.data) {
                    return searching
                } else {
                    searching = searching.next;
                }
            }
        } catch(e) {
            return 'Node not in list';
        }
    }

    remove(data) {
        let current_node = this.head;
        let previous_node = null;
        let found = false;
        if(!current_node) {
            return undefined;
        }
        while(current_node && !found) {
            if(data === current_node.data) {
                found = true;
            } else {
                previous_node = current_node;
                current_node = current_node.next;
            }
        }
        if(current_node === this.head) {
            this.pop();
        } else if(current_node.next === null) {
            previous_node.next = null;
        } else {
            previous_node.next = current_node.next;
        }
        this.size -= 1;
    }
}

module.exports = LinkedList;