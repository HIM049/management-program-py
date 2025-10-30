

class TableRow(list[str]):
    def length(self) -> int:
        return len(self)

class TableLayout:
    _rows: list[TableRow]
    _header: TableRow | None
    _lines: int

    def __init__(self, lines: int):
        self._rows = []
        self._lines = lines
        self._header = None

    def append_row(self, row: TableRow):
        if row.length() != self._lines:
            raise ValueError("lines mismatching")
        self._rows.append(row)

    def append_blank_row(self):
        row = TableRow([""] * self._lines)
        self.append_row(row)

    def set_header(self, header: TableRow):
        if header.length() != self._lines:
            raise ValueError("lines mismatching")
        self._header = header
            
    def print(self):
        table: list[TableRow] = []
        if self._header != None:
            table.append(self._header)
        table.extend(self._rows.copy())
            
        print_table(self._lines, table, self._header != None)

class Table:
    content: list[TableLayout]

    def __init__(self):
        self.content = []

    def append_layout(self, layout: TableLayout):
        self.content.append(layout)

    def print(self):
        for layout in self.content:
            layout.print()

def print_table(lines: int, data: list[TableRow], divider: bool):
    # the frame for lines
    row_template: str = ""
    for _ in range(lines):
        row_template += "{:<18}"

    header = data[0]
    print(row_template.format(*header))

    if divider:
        print("-" * (lines * 18))
    
    for row in data[1:]:
        content: list[str] = [] 
        for c in row:
            content.append(str(c))
        print(row_template.format(*content))