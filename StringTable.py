from ColumnWidthSolver import ColumnWidthSolver


class StringTable():
    
    def __init__(self, space = 3, indent = 3, width = 77):
        self.space   = space
        self.indent  = indent
        self.width   = width
        self.columns = 0
        self.rows    = []

    def text_line(self, *args):
        self.rows.append([])
        for arg in args:
            self.rows[-1].append(str(arg))
        if len(self.rows[-1]) > self.columns:
            self.columns = len(self.rows[-1])


    def draw(self):
        if self.columns == 0:
            return
        for i in range(len(self.rows)):
            if len(self.rows[i]) < self.columns:
                set_value(self.rows[i], self.columns - 1, "", "")
        
        required_space      =  0
        max_value_in_column = [0] * self.columns
        for column in range(self.columns):
            max_value = 0
            for row in range(len(self.rows)):
                if len(self.rows[row][column]) > max_value_in_column[column]:
                    max_value_in_column[column] = len(self.rows[row][column])
            required_space += max_value_in_column[column] 

        if required_space + self.indent + self.space * (self.columns - 1) <= self.width:
            for row in range(len(self.rows)):
                line = ' ' * self.indent + self.rows[row][0]
                for column in range(1, self.columns):
                    line += ' ' * (self.space + max_value_in_column[column-1] - len(self.rows[row][column-1])) + self.rows[row][column] 
                print line

        else:
            # Preparing v and c
            v = []
            for row in range(len(self.rows)):
                v.append([0] * self.columns)
                for column in range(self.columns):
                    v[row][column] = len(self.rows[row][column])
            c = self.width - self.indent - (self.columns - 1) * self.space
      
            x = ColumnWidthSolver(v,c).get_column_width()

            for i in range(len(self.rows)):
                activated = True
                for j in range(self.columns): 
                    if len(self.rows[i][j]) > x[j]:
                        activated = False
                if activated:
                    line = ' ' * self.indent + self.rows[i][0]
                    for j in range(1, self.columns):
                        line += ' ' * (self.space + x[j-1] - len(self.rows[i][j-1])) + self.rows[i][j]
                    print line
                else:
                    line = ""
                    for j in self.rows[i]:
                        line += j + " "
                    print line
                    


def set_value(liste, index, value, gap_fill = 0):
    if index >= len(liste):
        liste += [gap_fill] * (index - len(liste) + 1)
    liste[index] = value







