import { Node } from "./mynodes.js";


export class Stack {
    constructor(value){
        newnode = new Node(value);
        this.top = newnode
        this.height = 1
    }


    print_stack(){
        if (this.top == null){
            return
        }
        temp = this.top
        while (temp != null){
            console.log(temp.value)
            temp = temp.next
        }
    }


    push(value) {
        var newnode = new Node(value);
        if (this.top == null) {
            this.top = newnode;
            this.height += 1;
            return
        }
        newnode.next = this.top
        this.top = newnode
        this.height += 1
    }

    pop() {
        if (this.height == 0) {
            return
        }
        temp = this.top.next;
        this.top.next = null;
        this.top = temp;
        this.height -= 1
    }

}
