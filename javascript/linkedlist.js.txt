import { Node } from "./mynodes.js";

export class LinkedList {
    constructor(value) {
        var newnode = new Node(value);
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
        if (this.head == null) {
            return null
          };
        var newnode = new Node(value);
        this.tail.next = newnode;
        this.tail = newnode;
        this.length += 1
    }
    pop(){ 
        if (this.length == 0) {
            return null;
          } else if (this.length == 1) {
            this.head = null;
            this.tail = null;
          } else {
            temp = this.head
            while(temp.next !== this.tail){
                temp = temp.next
            };
            temp.next = null
            this.tail = temp
          }
        this.length -= 1

    }

    prepend(value) {
        var newnode = new Node(value)
        if (this.head == null) {
            this.head = newnode;
            this.tail = newnode;
        } else {
            newnode.next = this.head;
            this.head = newnode;
        }
        this.length += 1

    }

    pop_first() {
        if (this.length == 0) {
            return null
        } else if (this.length == 1) {
            this.head = null;
            this.tail = null;
        } else {
            temp = this.head;
            this.head = temp.next;
            temp.next = null;
        };
        this.length -= 1
    }



    get(index) {
        if (index > this.length || index < 0 ) {
            return false;
        }; 
        if (this.length == 0) {
            return null
        };
        temp = this.head;
        for (let i = 0; i < index; i++) {
            temp = temp.next;
        }; return temp;
    }

    remove(index) {  
        if (index > this.length || index < 0 ) {
            return false;
        }
        if (this.length == 0) {
            return null
        };
        if (index == 0) {
            this.pop_first()
        } else if (index == this.length) {
            this.pop()
        } else {
            before = this.get(index-1);
            temp = before.next;
            before.next = temp.next;
            temp.next = null
        }
        this.length -= 1
    };

    get_value(index){
        if (index > this.length || index < 0 ) {
            return false;
        }
        if (this.length == 0) {
            return null
        };
        temp = this.get(index);
        return temp.value;
    }

    set_value(index,value){
        if (index > this.length || index < 0 ) {
            return false;
        }
        if (this.length == 0) {
            return null
        };
        temp = this.get(index);
        temp.value = value
    }

    }
