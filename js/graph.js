class Graph {
    constructor() {
        this.nodes = {};
        this.size = 0;
    }

    stringToInt(stringArray) {
        let intArray = [];
        for(let i = 0; i < stringArray.length; i++) {
            intArray.push(+stringArray[i])
        }
        return intArray;
    }

    getNodes() {
        return this.stringToInt(Object.keys(this.nodes));
    }

    edges() {
        let edgeList = [];
        let key_list = this.stringToInt(Object.keys(this.nodes));
        if(key_list.length != 0) {
            for(let i = 0; i < key_list.length; i ++) {
                if(this.neighbors(key_list[i]).length != 0) {
                    let n_list = this.neighbors(key_list[i]);
                    for(let x = 0; x < n_list.length; x++) {
                        edgeList.push(key_list[i]);
                        edgeList.push(n_list[x]);   
                    }
                }
            }
        return edgeList;
        } else {
            return 'No edges in graph';
        }
    }

    addNode() {
        for (var i = 0; i < arguments.length; i++) {
            if(this.nodes[arguments[i]] === undefined) {
                this.nodes[arguments[i]] = [];
                this.size += 1;
            } 
        }
    }

    addEdge(data1, data2) {
        this.addNode(data1, data2);
        if(!this.nodes[data1].includes(data2)) {
            this.nodes[data1].push(data2);
        }
    }

    delNode(data) {
        let key_list = this.stringToInt(Object.keys(this.nodes));
        if(key_list.includes(data)) {
            let index = key_list.indexOf(data);
            key_list.splice(index, 1);
            delete this.nodes[data];
            this.size -= 1;
        } else {
            return 'No such node';
        }
        for(let i = 0; i < key_list.length; i++) {
            if(this.nodes[key_list[i]].includes(data)) {
                let index = this.nodes[key_list[i]].indexOf(data);
                this.nodes[key_list[i]].splice(index, 1);
            }
        }
    }

    delEdge(data1, data2) {
        if(this.adjacent(data1, data2) === true) {
            let index = this.nodes[data1].indexOf(data2);
            this.nodes[data1].splice(index, 1);
        } else {
            return 'Edge not in graph';
        }
    }

    hasNode(data) {
        let key_list = this.stringToInt(Object.keys(this.nodes));
        return key_list.includes(data);
    }

    neighbors(data) {
        if(this.hasNode(data)) {
            return this.nodes[data];
        } else {
            return 'No such node';
        }
    }

    adjacent(data1, data2) {
        if(this.hasNode(data1) && this.hasNode(data2)) {
            return this.neighbors(data1).includes(data2);
        } else {
            return 'Both nodes not in graph'
        }
    }
}

module.exports = Graph;