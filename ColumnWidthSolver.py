class ColumnWidthSolver():

    def __init__(self, v, c):
        self.v = v               # Matrix with dim(nr_of_lines,nr_of_columns)
        self.c = c               # Width of the Window
        self.n = len(v)          # nr_of_lines
        self.m = len(v[0])       # nr_of_columns
        self.I = range(self.n) 	 # IndexList of activated lines

    def get_column_width(self):

        max_v = self.max_v()
        p = sum(max_v) - self.c
        h = []
        for i in range(p):
            h.append([0] * self.m)

        while p > 0:

            # --- Find j* and x* ---
            maximum = 0
            max_j = 0
            for j in range(self.m):
                for i in self.I:
                    if max_v[j] - self.v[i][j] < p:
                        h[max_v[j] - self.v[i][j]][j] += 1

                lines = 0
                for i in range(p):
                    lines += h[i][j]
                    if maximum < (i+1)/lines:
                        maximum = (i+1)/lines
                        max_j = j

            # --- delete lines
            delete_line = []
            for i in self.I:
                if max_v[max_j] - self.v[i][max_j] < p:
                    delete_line.append(i)
            self.I = list(set(self.I) - set(delete_line))

            # --- Calcuate new p
            max_v = self.max_v()
            p = sum(max_v) - self.c

        return max_v

    # Vector of maximal value in each column in v
    def max_v(self):
        return list((max(self.v[i][j] for i in self.I)) for j in range(self.m))
