import { Node } from "./mynodes.js";


export class Queue {


    constructor(value){
        var newnode = new Node(value);
        this.front = newnode;
        this.rear = newnode;
        this.length = 1;
    }


    print_queue(){
        if (this.front == null) {
            return null
        }

        temp = this.front;
        while(temp != null) {
            console.log(temp.value);
            temp = temp.next
        }
    }

    enqueue(value){
        var newnode = new Node(value);
        if (this.length == 0) {
            this.rear = newnode;
            this.front = newnode;
        } else {
            this.rear.next = newnode;
            this.rear = newnode;
        }
        this.length += 1
    }
    

    dequeue(){
        if(this.length == 0) {
            return
        }
        temp = this.front;
        if(this.length == 1) {
            this.rear = null;
            this.front = null;
        } else {
            this.front = this.front.next;
            temp.next = null;
        }
        this.length -= 1
    }
}

