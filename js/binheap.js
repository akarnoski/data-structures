class BinHeap {
    constructor() {
        this.heap_list = []
        this.size = 0;
    }

    push(data) {
        this.heap_list.push(data);
        if(this.heap_list.length === 2) {
            this.small_heap();
        } else {
            this.check_heap()
        }
        this.size += 1;
    }

    small_heap() {
        let heap = this.heap_list;
        if(heap[0] > heap[1]) {
            let bigger = heap[0];
            heap[0] = heap[1];
            heap[1] = bigger;
        }
        return heap;
    }

    check_heap() {
        let heap = this.heap_list;
        let index = Math.floor((heap.length - 1) / 2);
        let i = 0
        while(i < index) {
            let l = (2 * i) + 1;
            if(heap[i] > heap[l]) {
                let bigger = heap[i];
                heap[i] = heap[l];
                heap[l] = bigger;
            }
            try {
                let r = (2 * i) + 2;
                if(heap[i] > heap[r]) {
                    bigger = heap[i];
                    heap[i] = heap[r];
                    heap[r] = bigger;
                }
            } catch(e) {
                pass;
            }
            i += 1;
        }
        return heap
    }

    pop() {
        try {
            let heap = this.heap_list;
            let index = heap.length - 1;
            let zero = heap[0];
            heap[0] = heap[index];
            heap[index] = zero;
            this.heap_list.pop();
            if(this.heap_list.length == 2) {
                self._small_heap();
            }
            this.check_heap();
            return heap;
        } catch(e) {
            return 'Nothing available to pop';
        }
    }
}

module.exports = BinHeap;