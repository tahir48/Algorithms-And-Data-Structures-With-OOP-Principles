import { LinkedList } from "./linkedlist.js"


var mylinkedlist = new LinkedList(0)
mylinkedlist.append(1)
mylinkedlist.append(2)
mylinkedlist.append(3)
mylinkedlist.append(4)
mylinkedlist.append(5)
mylinkedlist.append(6)
// mylinkedlist.remove(6)
// mylinkedlist.pop_first()
// mylinkedlist.prepend()
// mylinkedlist.pop()
//mylinkedlist.set_value(3,300)




//render these
{mylinkedlist.print_list()}; 
{console.log("get method", mylinkedlist.get(2).value)};

