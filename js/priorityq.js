class PriorityQueue {
    constructor() {
        this.priority_dict = {};
        this.max = null;
    }

    insert(data, priority=0) {
        if(this.priority_dict[priority] === undefined) {
            this.priority_dict[priority] = [data];
        } else {
            this.priority_dict[priority].push(data);
        }
        this.getMax();
    }

    getMax() {
        let priority_list = Object.keys(this.priority_dict);
        if(priority_list.length != 0) {
            let max = 0;
            for(let i = 0; i < priority_list.length; i++) {
                if (priority_list[i] > max) this.max = parseInt(priority_list[i]);
            }
        } else {
            this.max = null;
        }
    }

    pop() {
        if(this.max === null) {
            return 'Nothing to pop';
        } else {
            let popped = this.priority_dict[this.max].shift();
            if(this.priority_dict[this.max].length === 0) {
                delete this.priority_dict[this.max];
                this.getMax();
            }
            return popped;
        }
    }

    peek() {
        if(this.max === null) {
            return 'None';
        } else {
            return this.priority_dict[this.max][0];
        }
    }
}

module.exports = PriorityQueue;