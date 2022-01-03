export class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }


export class DNode {
  constructor(value) {
    this.value = value
    this.next = null;
    this.prev = null;
  }
}


export class TreeNode{
  constructor(value) {
    this.value = value;
    this.right = null;
    this.left = null;
  }
}