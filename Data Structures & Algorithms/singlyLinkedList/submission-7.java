//Singly Linked List 
class Node {
    //class variables 
    int val; 
    Node next; 

    //Constrctor 
    public Node(int val){
        this.val = val; 
        this.next = null;
    }

    //Constrctor - set next to null
    public Node(int val, Node next){
        this.val = val; 
        this.next = next; 
    }
}

class LinkedList {
    //class variables 
    private Node head; 
    private Node tail; 

    public LinkedList() {
        //create a list dummy list node for head and tail 
        this.head = new Node(-1);
        this.tail = this.head;
    }

    public int get(int index) {
        Node curr = head.next; 
        while (curr != null && index > 0) {
            curr = curr.next; 
            index = index - 1; 
        }
        if (curr == null) {
            return - 1;
        } else {
            return curr.val;
        }
    } 
    
    public void insertHead(int val) {
        Node newNode = new Node(val); 
        newNode.next = head.next; 
        head.next = newNode; 

        //edge case where list is empty
        if (newNode.next == null){
            tail = newNode;
        }
        
    }

    public void insertTail(int val) {
        // Attach at end
        Node newNode = new Node(val);
        this.tail.next = newNode; 

        // Move pointer
        this.tail = this.tail.next; 

    }

    public boolean remove(int index) {
        //start from the head
        Node curr = this.head; 

        //iterate 
        while (index > 0 && curr != null){
            index = index - 1; 
            curr = curr.next; 
        }

        // remove 
        if (curr != null && curr.next != null) {
            if (curr.next == this.tail) {
                this.tail = curr;
            }
            curr.next = curr.next.next; 
            return true; 
        }
        return false;
        
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<>(); 
        Node curr = head.next; 

        while(curr != null){ 
            values.add(curr.val); 
            curr = curr.next;
        }

        return values; 

    }
}
