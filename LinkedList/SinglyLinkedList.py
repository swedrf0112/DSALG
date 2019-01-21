'''
實作 Singly Linked List, 包含操作等方法如下:
getAtIndex, getAtHead, getTail
addAtIndexBefore, addAtIndexAfter
deleteAtIndex, deleteAtHead, deleteAtTail
print

詳細註解可參考:
https://github.com/swedrf0112/Leetcode/blob/master/707_Design_Linked_List/MyLinkedList.py
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
		
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def getAtHead(self):
        return self.getAtIndex(0)
        
    def getAtTail(self):
        return self.getAtIndex(self.size-1)
        
    def getAtIndex(self, index):
        if index < 0 or index >= self.size:
            return 
			
        if self.head is None:
            return
        
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        
        return ptr.val
            
    def addAtHead(self, val):
        self.addAtIndexBefore(0, val)
        
    def addAtTail(self, val):
        self.addAtIndexBefore(self.size, val)
    
    def addAtIndexBefore(self, index, val):
        if index < 0 or index > self.size:
            print("Invalid index")
            return
        
        newnode = Node(val)
        if index == 0:
            newnode.next = self.head
            self.head = newnode
        else:
            ptr = self.head
            for _ in range(index - 1):
                ptr = ptr.next
            
            newnode.next = ptr.next
            ptr.next = newnode
            
        self.size += 1
    
    def addAtIndexAfter(self, index, val):
        if index < 0 or index > self.size:
            print("Invalid index")
            return
        
        newnode = Node(val)
        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        
        newnode.next = ptr.next
        ptr.next = newnode

        self.size += 1
        
    def deleteAtHead(self):
        self.deleteAtIndex(0)
        
    def deleteAtTail(self):
        self.deleteAtIndex(self.size - 1)
            
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            ptr = self.head
            for _ in range(index - 1):
                ptr = ptr.next
                
            ptr.next = ptr.next.next
            
        self.size -= 1
                
    def print(self):
        ptr = self.head

        while ptr != None:
            print("[%d]" % ptr.val, end = "")
            ptr = ptr.next            
		
        print()
		
		
'''
l1 = SinglyLinkedList()
l1.addAtHead(1)
l1.addAtTail(3)
l1.print()
l1.addAtIndexBefore(0, 111)
l1.print()
l1.addAtIndexAfter(0, 222)
l1.print()
l1.addAtIndexAfter(1, 999)
l1.print()

l1.deleteAtHead()
l1.print()
l1.deleteAtTail()
l1.print()
l1.deleteAtIndex(1)
l1.print()
-----------------------------------------
[1][3]
[111][1][3]
[111][222][1][3]
[111][222][999][1][3]
[222][999][1][3]
[222][999][1]
[222][1]
'''


'''
print(l1.getAtIndex(0))
print(l1.getAtHead())
print(l1.getAtTail())
-----------------------------------------
222
222
1
'''