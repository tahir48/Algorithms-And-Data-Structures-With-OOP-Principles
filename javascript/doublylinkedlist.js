import { DNode } from "./mynodes.js";


export class DoublyLinkedList {
    constructor(value) {
        var newnode = new DNode(value);
        this.head = newnode;
        this.tail = newnode;
        this.length = 1;
    }

    print_list() {
        temp = this.head;
        while (temp !== null) {
            console.log(temp.value);
            temp = temp.next;
            }
    }

    append(value){
        var newnode = new DNode(value)
        if (this.length == 0) {
            this.head = newnode
            this.tail = newnode
        } else {
            this.tail.next = newnode
            newnode.prev = newnode
            this.tail = newnode
        }
        this.length += 1
    }

    
    pop() {
        if (this.length == 0) {
            return null
        }if (this.length == 1) {
            this.head = null;
            this.tail = null;
        } else {
            temp = this.tail;
            this.tail = temp.prev;
            temp.prev = null;
            this.tail.next = null;
        } 
        this.length -= 1
    }

    
    prepend(value) {
        var newnode = new DNode(value);
        if (this.head  == null) {
            this.head = newnode
            this.tail = newnode
        } else {
            newnode.next = this.head;
            this.head.prev = newnode;
            this.head = newnode
        }
        this.length += 1
    }
    
        
            
    pop_first() {
        if (this.length == 0) {
            return
        } else if (this.length == 1) {
            this.head = null;
            this.tail = null;
        } else {
            temp = this.head;
            this.head = temp.next;
            temp.next = null
        }
        this.length -= 1
    }
    
    

    get(index) {
        if (index > this.length || index <0) {
            return false
        }
        if (this.length == 0) {
            return
        }
        temp = this.head;
        if (index < this.length / 2) {
            for (var i=0; i < index ;i++) {
                temp = temp.next;
            }     
        } else {
            temp = this.tail;
            for(var i = this.length-1; i>index ; i--){
                temp = temp.prev
            }
        }
        return temp.value
    }
    
    remove(index) {
        if (index > this.length || index <0) {
            return false
        }
        if (this.length == 0) {
            return null
        }
        if (index == 0) {
            this.pop_first()
        } else if (index == this.length) {
            this.pop()
        } else {
            before = this.get(index - 1);
            temp = before.next;
            before.next = temp.next;
            temp.next.prev = before;
            temp.next = null;
            temp.prev = null
        }
        this.length -= 1
    }
        
    
    set_value(index,value) {
        if (index > this.length || index <0) {
            return false
        }
        if (this.length == 0) {
            return null
        }
        temp = this.get(index);
        temp.value = value
    }
}
