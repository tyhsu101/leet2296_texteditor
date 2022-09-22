class TextEditor:

    def __init__(self):
        self.cursor_point = 0
        self.text = ''
    def addText(self, text: str) -> None:
        self.text =  self.text[0:self.cursor_point] + text + self.text[self.cursor_point:]
        self.cursor_point += len(text)

    def deleteText(self, k: int) -> int:
        if self.cursor_point - k >= 0:
            self.text = self.text[0:self.cursor_point - k] + self.text[self.cursor_point:]
            self.cursor_point -= k
        else:
            self.text = self.text[self.cursor_point:]
            self.cursor_point = 0
    def cursorLeft(self, k: int) -> str:
        if self.cursor_point - k >= 0:
            self.cursor_point -=k 
        else:
            self.cursor_point = 0
        self.print_cursor_place()
    
    def cursorRight(self, k: int) -> str:
        if self.cursor_point + k <= len(self.text):
            self.cursor_point +=k 
        else:
            self.cursor_point = len(self.text)
        self.print_cursor_place()
    
    def print_cursor_place(self):
        print(self.text[max(self.cursor_point-10,0):self.cursor_point] + '*|*' + self.text[self.cursor_point:min(self.cursor_point+10,len(self.text))])


    def __str__(self):
        return self.text