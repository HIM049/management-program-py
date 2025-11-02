

class TableRow(list[str]):
    def length(self) -> int:
        return len(self)

class TableLayout:
    _title: str
    _header: TableRow | None
    _rows: list[TableRow]
    _lines: int

    def __init__(self, lines: int):
        self._rows = []
        self._lines = lines
        self._header = None
        self._title = ""

    def append_row(self, row: TableRow):
        if row.length() != self._lines:
            raise ValueError("lines mismatching")
        self._rows.append(row)

    def set_rows(self, rows: list[TableRow]):
        self._rows = rows

    def append_blank_row(self):
        row = TableRow([""] * self._lines)
        self.append_row(row)

    def set_header(self, header: TableRow):
        if header.length() != self._lines:
            raise ValueError("lines mismatching")
        self._header = header

    def set_title(self, title: str):
        self._title = title

    def get_lines(self) -> int:
        return self._lines
            
    def print(self):
        table: list[TableRow] = []
        
        if self._header != None:
            table.append(self._header)
        table.extend(self._rows.copy())
        print_table(self._lines, table, self._title, self._header != None)

class Table:
    _content: list[TableLayout]
    _title: str
    _end_divider: bool

    def __init__(self):
        self._content = []
        self._title = ""
        self._end_divider = False

    def append_layout(self, layout: TableLayout):
        self._content.append(layout)

    def set_title(self, title: str):
        self._title = title

    def set_end_divider(self, need_divider: bool):
        self._end_divider = need_divider

    def get_max_lines(self) -> int:
        max_lines: int = 0
        for item in self._content:
            max_lines = max(max_lines, item.get_lines())
        return max_lines

    def print(self):
        max_lines = self.get_max_lines()
        if len(self._title) > 0:
            divider_length = (max_lines * 18 - len(self._title) - 2) // 2
            print("-" * divider_length, self._title, "-" * divider_length)
        for layout in self._content:
            layout.print()
        if self._end_divider:
            print("-" * max_lines * 18)

def print_table(lines: int, data: list[TableRow], title: str, divider: bool):
    if len(title) > 0:
        title_divider_length = ((lines * 18 - len(title) - 2) // 2)
        print("-"*title_divider_length, title, "-"*title_divider_length)
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