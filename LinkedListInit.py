class Node(object):
    def __init__(self, title = None, time = None, nextNode = None):
        self.title = title
        self.time = time
        self.nextNode = nextNode

    def return_title(self):
        return self.title

    def return_time(self):
        return self.time

    def get_next(self):
        return self.nextNode

    def set_next(self, new):
        self.nextNode = new


class LinkedList(object):
    def __init__(self, front = None):
        self.front = front

    def insert(self, title, time):
        new_node = Node(title, time)
        new_node.set_next(self.front)
        self.front = new_node

    def printData(self):
        curr = self.front
        while curr != None:
            print 'Title: ' + str(curr.return_title()), '\nTime To Cook: ' + str(curr.return_time()), 'minutes'
            print '\n'
            curr = curr.get_next()

    def dataToFile(self):
        end_string = ''
        curr = self.front
        while curr != None:
            end_string = end_string + str(curr.return_title()) + ' ' + str(curr.return_time()) + '\n'
            curr = curr.get_next()
        return end_string
