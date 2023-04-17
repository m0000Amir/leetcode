
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

/**
 * 
 * @param {Array} link 
 * @returns 
 */
function prepareLink(link) {
    let head = new ListNode(link[0]);
    for (let i = 1; i<= link.length - 1; i++) {
        let node = head
        while (node.next) node = node.next;
        node.next = new ListNode(link[i]);
    }
    return head
}

/**
 * 
 * @param {ListNode} head 
 */
function printLinkedList(head) {
    console.log("[ ")
    let ptr = head;
    while (ptr) {
        console.log(ptr.val,",");
        ptr = ptr.next;
    }
    console.log("]");
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
 var addTwoNumbers = function(l1, l2) {
    let head = null;
    let prev = null;
    let temp = null;
    let carry = 0;

    // while tw list exists
    while (l1 !== null || l2 !== null) {
        let l1Val = l1 === null ? 0 : l1.val;
        let l2Val = l2 === null ? 0 : l2.val;

        let sum = carry + l1Val + l2Val;

        // update carry 
        carry = sum >= 10 ? 1 : 0;

        // update sum
        sum = sum < 10 ? sum : sum % 10;

        // create new node wih sum
        temp = new ListNode(sum);

        if (head === null) {
            head = temp;
        } else {
            prev.next = temp;
        }
        prev = temp;

        //  to the next child nodes of l1 and l2

        if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    }

    if (carry > 0){
        temp.next = new ListNode(carry);
    }

    return head;
};

l1 = prepareLink([2,4,9]);
printLinkedList(l1);

l2 = prepareLink([5,6,4,9]);
printLinkedList(l2);

let sol = addTwoNumbers(l1, l2);
printLinkedList(sol);