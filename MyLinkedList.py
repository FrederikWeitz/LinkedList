# MyLinkedList Class for Python Bootcamp tutorial - Video 225

# Class for internal Use (and really unspecified)
# stores a Dictionary and a possible Link to another Member
class Member():

    def __init__(self):
        """Creates empty Instance"""
        self.member = None
        self.link = None

    def setMember(self, pointer):
        """stores Content"""
        if type(pointer)==dict:
            self.member = pointer
        else:
            self.member = {}

    def getMember(self):
        """returns Content"""
        return self.member

    def setLink(self, link):
        """links to another Instance of Member"""
        if type(link)==Member or link==None:
            self.link = link
            return True
        else:
            return False

    def getLink(self):
        """returns content of a Link"""
        return self.link



# A linked list with various methods to handle instances of the member-Class
# Methods to add
#     .add(), .add_many(), .add_after(), .add_before()
# Methods to remove
#     .remove(), .pop_head(), .pop_tail(), .pop_at_index()
# Methods to find
#     .has(), .has_at_index(), .has_key(), .has_keys(), .has_member(), .has_dict(), .has_dict_keys()
# Length of the LinkedList
#     .len()
# Cloning a Member of the List
#     .clone()

class LinkedList():
    """One-direction mutable LinkedList for various dictionaries
    contains Methods to add, remove and search"""
    def __init__(self):
        self.head = None
        self.tail = self.head

    def add(self, member, clone=True):
        """ adds a previously created Member by cloning it or a Dictionary by creating a new member,
        if you want to add a Member without cloning, add clone=0 in parameters"""
        if type(member)==Member:
            if clone:
                member = dict([(x,y) for x,y in member.getMember().items()])
            else:
                if self.head:
                    self.tail.setLink(member)
                    self.tail = member
                else:
                    self.tail = member
                    self.head = member 
        if type(member)==dict:
            temp = Member()
            temp.setMember(member)
            member = temp
            if self.head:
                self.tail.setLink(member)
                self.tail = member
            else:
                self.tail = member
                self.head = member

    def add_many(self, pointerList):
        """adds a list of either Members and Dictionaries"""
        if type(pointerList)==list:
            [self.add(x) for x in pointerList]

    # nur zwei Methoden zur besseren Überprüfung
    def print(self, index):
        """prints content of Member at given index"""
        count=0
        start = self.head
        while start:
            if count==index:
                print(count, ' : ', start.getMember())
                break
            start=start.getLink()
            count+=1

    def printAll(self):
        """prints whole list"""
        start = self.head
        while start:
            print(start.getMember())
            start=start.getLink()
            
    def has_member(self, pointer):
        """returns True if pointer is member of the list"""
        start = self.head
        while start:
            if start==pointer:
                return True
            start = start.getLink()
        return False

    def has_at_index(self, index):
        """returns member at given index"""
        count = 0
        start = self.head
        while start:
            if count==index:
                return start
            start = start.getLink()
            count+=1
        return None

    def has_key(self, key_in_pointer):
        """returns first member, whose dictionary contains given key"""
        start = self.head
        while start:
            if key_in_pointer in start.getMember().keys():
                return start
            start = start.getLink()
        return None

    def has_keys(self, key_in_pointer):
        """returns list of all members, whose dictionaries contain given key"""
        start = self.head
        rList = []
        while start:
            if key_in_pointer in start.getMember().keys():
                rList.append(start)
            start = start.getLink()
        return rList

    def has_dict(self, dict_in_pointer):
        """returns member, whose dictionary is equal to given dictionary"""
        if type(dict_in_pointer)!=dict:
            return None
        start = self.head
        while start:
            if dict_in_pointer==start.getMember():
                return start
            start = start.getLink()
        return None

    def has_dict_keys(self, dict_in_pointer):
        """returns first member whose dictionary-keys are equal to the given dictionary-keys,
        a list of strings or one string"""
        if type(dict_in_pointer)==str:
            dict_in_pointer = [dict_in_pointer]
        if type(dict_in_pointer)==dict:
            dict_in_pointer = dict_in_pointer.keys()
        if type(dict_in_pointer)!=list:
            return None
        start = self.head
        while start:
            if dict_in_pointer==start.getMember():
                return start
            start = start.getLink()
        return None

    def len(self):
        """returns length of the list"""
        start = self.head
        count = 0
        while start:
            count+=1
            start = start.getLink()
        return count

    def remove(self, pointer=None, index=None, data=None):
        """removes an element either by pointer (to a member), index or data
        data must be equal in every part
        returns removed Member-instance or None"""
        def rPointer(pointer):
            start = self.head
            if start==pointer:
                self.head = self.head.getLink()
                return start
            while start:
                if start.getLink()==None:
                    return None
                if start.getLink()==pointer:
                    temp=start.getLink()
                    start.setLink(temp.getLink())
                    return temp
                start = start.getLink()

        def rIndex(index):
            start = self.head
            count = 0
            if index == count:
                self.head = start.getLink()
                return start
            while count < index-1:
                start = start.getLink()
                if not start:
                    return None
                count+=1
            else:
                temp=start.getLink()
                start.setLink(temp.getLink())
                return temp

        def rData(data):
            start = self.head
            if start.getMember()==data:
                self.head = start.getLink()
                return start
            while start:
                if start.getLink().getMember()==data:
                    temp=start.getLink()
                    start.setLink(temp.getLink())
                    return temp
                start = start.getLink()
            return None
                
        if pointer and type(pointer)==Member:
            return rPointer(pointer)
        if index and type(index)==int:
            return rIndex(index)
        if data and type(data)==dict:
            return rData(data)
        return None

    def add_after(self, pointer, member=None, index=None,clone=True):
        """adds a new member after a given member or index
        clones the instance, add clone=False, if not desired"""
        if not(type(pointer)==Member or type(pointer)==dict):
            return False
        else:
            if type(pointer)==dict:
                temp = Member()
                temp.setMember(pointer)
                pointer = temp
            else:
                if clone:
                    temp = Member()
                    temp.setMember(dict([(x,y) for x,y in pointer.getMember().items()]))
                    pointer=temp
        
        if member and type(member)==Member:
            start = self.head
            while start:
                if start==member:
                    temp = start.getLink()
                    start.setLink(pointer)
                    pointer.setLink(temp)
                    if pointer.getLink()==None:
                        self.tail=pointer
                    return True
                start = start.getLink()
            return False
        
        if type(index)==int:
            count=0
            start=self.head
            while count<index:
                count+=1
                start=start.getLink()
                if not start:
                    return False
            else:
                 temp = start.getLink()
                 start.setLink(pointer)
                 pointer.setLink(temp)
                 if pointer.getLink()==None:
                        self.tail=pointer
                 return True
        return False

    def add_before(self, pointer, member=None, index=None, clone=True):
        """adds a new member before a given member or index
        clones the instance, add clone=False, if not desired"""
        if not(type(pointer)==Member or type(pointer)==dict):
            return False
        else:
            if type(pointer)==dict:
                temp = Member()
                temp.setMember(pointer)
                pointer = temp
            else:
                if clone:
                    temp = Member()
                    temp.setMember(dict([(x,y) for x,y in pointer.getMember().items()]))
                    pointer=temp
        
        if member and type(member)==Member:
            start = self.head
            if start==member:
                pointer.setLink(start)
                self.head=pointer
                return True
            while start:
                if start.getLink()==member:
                    temp = start.getLink()
                    start.setLink(pointer)
                    pointer.setLink(temp)
                    if pointer.getLink()==None:
                        self.tail=pointer
                    return True
                start = start.getLink()
            return False
        
        if type(index)==int:
            if index==0:
                pointer.setLink(self.head)
                self.head=pointer
                return True
            count=0
            start=self.head
            while count<index-1:
                count+=1
                start=start.getLink()
                if not start:
                    return False
            else:
                temp = start.getLink()
                start.setLink(pointer)
                pointer.setLink(temp)
                if pointer.getLink()==None:
                    self.tail=pointer
                return True
        return False

    def pop_tail(self):
        """pops last element (tail of the list)"""
        if self.head==None:
            return None
        if self.head.getLink()==None:
            temp=self.head
            self.head=None
            self.tail=None
            return temp
        start=self.head
        while start.getLink().getLink()!=None:
            start=start.getLink()
        temp = start.getLink()
        start.setLink(None)
        self.tail=start
        return temp

    def pop_head(self):
        """pops first element (head of the list)"""
        if self.head==None:
            return None
        if self.head.getLink()==None:
            temp=self.head
            self.head=None
            self.tail=None
            return temp
        temp = self.head
        self.head=self.head.getLink()
        return temp

    def pop_at_index(self, index):
        """pops element at given index"""
        if index==0:
            return self.pop_head()
        count=0
        start=self.head
        while count<index-1:
            start=start.getLink()
            count+=1
            if start.getLink()==None:
                return None
        temp=start.getLink()
        if temp.getLink()==None:
            return  self.pop_tail()
        start.setLink(temp.getLink())
        return temp

    def clone(self, index=None, data=None):
        """clones Member at index or first where one key of Member-dictionary fits to data-String"""
        if index and type(index)==int:
            start=self.head
            count=0
            while count<index:
                start=start.getLink()
                count+=1
                if start==None:
                    return None
            temp = Member()
            temp.setMember(dict([(x,y) for x,y in start.getMember().items()]))
            return temp
        if data:
            start = self.has_Key(data)
            temp = Member()
            temp.setMember(dict([(x,y) for x,y in start.getMember().items()]))
            return temp
