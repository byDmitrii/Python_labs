from StackClass import Stack
from DequeClass import Deque
import random


with open('book.txt', 'r') as books:
    books = open('book.txt', 'r', encoding="utf8")
    q1 = Deque()
    q2 = Deque()
    lines = books.readlines()

    for i in range(len(lines)):
        line = lines[i]
        if q1.is_empty():
            q1.push(line)
        elif line <= q1.peek_left():
            q1.push_left(line)
        elif line >= q1.peek():
            q1.push(line)
        else:
            while not q1.is_empty():
                e = q1.pop_left()
                if e < line:
                    q2.push(e)
                else:
                    q2.push(line)
                    q2.push(e)
                    while not q1.is_empty():
                        q2.push(q1.pop_left())
                    break
            q1, q2 = q2, q1
    print("\nРешение задания №1\n")
    while not q1.is_empty():

        print(q1.pop_left())

with open('messageCODE.txt', encoding='utf-8') as message:
    lines = message.readlines()
    q1 = Deque()
    q2 = Deque()
    for s in lines:
        for c in s:
            q1.push(c)

    while not q1.is_empty():
        try:
            c: str = q1.pop_left()
            if c.isalnum():
                code = ord(c) - 1
                q2.push(chr(code))
            elif c == " ":
                q2.push(c)

        except e:
            print(e)

    buf = str()
    while not q2.is_empty():
        buf += q2.pop_left()
    print("\nЗадание №2\n")
    print(buf)


def tower_disk(number_of_disks, start, auxiliary, end):
    if number_of_disks == 1:
        print("Переместим диск 1 со стержня {} на стержень {}".format(start, end))
        return
    tower_disk(number_of_disks - 1, start, end, auxiliary)
    print('Переместили диск {} со стержня {} на стержень {}'.format(number_of_disks, start, end))
    tower_disk(number_of_disks - 1, auxiliary, start, end)

print("\nЗадание №3\n")
disks = int(input("\nСколько у вас дисков? \n"))

tower_disk(disks, 'A', 'B', 'C')

def check_brackets(string):
    bracket_stack = Stack()
    for i in string:
        if i == '(':
            bracket_stack.push(i)
        elif i == ')':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
    return bracket_stack.is_empty()

print("\nЗадание №4\n")
print(check_brackets('(())()('))
print(check_brackets('(((()())()()()()))'))

def check_square_brackets(string):
    bracket_stack = Deque()
    for i in string:
        if i == '[':
            bracket_stack.push(i)
        elif i == ']':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
    return bracket_stack.is_empty()
print("\nЗадание №5\n")
print(check_square_brackets('[[[]]]'))
print(check_square_brackets('[[][][]'))

print("\nЗадание №6\n")
with open('sentenceSORT.txt', encoding='utf-8') as file:
    text = str(file.readlines())
    print("\nТекст до сортировки: ")
    print(text)
    dig = Stack()
    let = Stack()
    oth = Stack()

    for c in text:
        if c.isalpha():
            let.push(c)
        elif c.isdigit():
            dig.push(c)
        else:
            oth.push(c)

    new_text = str()
    while not dig.is_empty():
        new_text += str(dig.pop_left())

    new_text += ""

    while not let.is_empty():
        new_text += str(let.pop_left())

    new_text += ""

    while not oth.is_empty():
        new_text += str(oth.pop_left())

    print("\nСортировка выполнена: ")
    print(new_text)

print("\nЗадание №7\n")
numbers = [random.randint(-50, 50) for i in range(20)]
print(numbers)
deque = Deque()
for n in numbers:
    if n < 0:
        deque.push_left(n)
    else:
        deque.push(n)
while not deque.is_empty():
    x = deque.pop_left()
    if x < 0:
        deque.push(x)
    else:
        deque.push_left(x)
        break
while not deque.is_empty():
    x = deque.pop()
    if x < 0:
        print(x)
    else:
        deque.push(x)
        break
while not deque.is_empty():
    print(deque.pop_left())


print("\nЗадание №8\n")
with open('book.txt', 'r') as books:
    books=open('book.txt','r', encoding='utf8')
    stack = Stack()
    for book in books:
        book = book.strip()
        print(book)
        stack.push(book)
    print()
    while not stack.is_empty():
        print(stack.pop())