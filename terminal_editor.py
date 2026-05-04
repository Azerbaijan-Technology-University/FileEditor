import curses
from pathlib import Path
from typing import Final


class Editor:
    EXIT_KEY: Final[int] = 17  # Ctrl+Q
    SAVE_KEY: Final[int] = 19  # Ctrl+S

    def __init__(self, stdscr, file_path: Path) -> None:
        self.stdscr = stdscr
        self.file_path = file_path
        self.buffer: list[str] = [""]

        if self.file_path.exists():
            content = self.file_path.read_text()
            self.buffer = content.splitlines() if content else [""]
        else:
            self.buffer = [""]

        self.row: int = 0
        self.col: int = 0
        self.top_line: int = 0

        curses.curs_set(1)
        self.stdscr.keypad(True)
        self.stdscr.nodelay(False)

        self.stdscr.move(self.row, self.col)
        self.stdscr.refresh()

    def save_file(self) -> None:
        try:
            content = "\n".join(self.buffer)
            self.file_path.write_text(content)
        except Exception:
            pass

    def render(self) -> None:
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()

        if self.row < self.top_line:
            self.top_line = self.row
        elif self.row >= self.top_line + height:
            self.top_line = self.row - height + 1

        for i in range(height):
            buffer_idx = self.top_line + i
            if buffer_idx < len(self.buffer):
                line = self.buffer[buffer_idx]
                try:
                    self.stdscr.addstr(i, 0, line[: width - 1])
                except curses.error:
                    pass

        try:
            self.stdscr.move(self.row - self.top_line, self.col)
        except curses.error:
            self.stdscr.move(0, 0)

        self.stdscr.refresh()

    def update(self) -> bool:
        key: int = self.stdscr.getch()

        if key == self.EXIT_KEY:
            return False

        if key == self.SAVE_KEY:
            self.save_file()
            return True

        # --- Router ---
        if key == curses.KEY_UP:
            self._move_up()
        elif key == curses.KEY_DOWN:
            self._move_down()
        elif key == curses.KEY_LEFT:
            self._move_left()
        elif key == curses.KEY_RIGHT:
            self._move_right()
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            self._handle_backspace()
        elif key in (curses.KEY_ENTER, 10, 13):
            self._handle_newline()
        elif 32 <= key <= 126:
            self._handle_text_input(chr(key))

        return True

    def _move_up(self) -> None:
        if self.row > 0:
            self.row -= 1
            self.col = min(self.col, len(self.buffer[self.row]))

    def _move_down(self) -> None:
        if self.row < len(self.buffer) - 1:
            self.row += 1
            self.col = min(self.col, len(self.buffer[self.row]))

    def _move_left(self) -> None:
        if self.col > 0:
            self.col -= 1

    def _move_right(self) -> None:
        if self.col < len(self.buffer[self.row]):
            self.col += 1

    def _handle_backspace(self) -> None:
        if self.col > 0:
            line: str = self.buffer[self.row]
            self.buffer[self.row] = line[: self.col - 1] + line[self.col :]
            self.col -= 1
        elif self.row > 0:
            prev_len: int = len(self.buffer[self.row - 1])
            self.buffer[self.row - 1] += self.buffer.pop(self.row)
            self.row -= 1
            self.col = prev_len

    def _handle_newline(self) -> None:
        remainder: str = self.buffer[self.row][self.col :]
        self.buffer[self.row] = self.buffer[self.row][: self.col]
        self.buffer.insert(self.row + 1, remainder)
        self.row += 1
        self.col = 0

    def _handle_text_input(self, char: str) -> None:
        line: str = self.buffer[self.row]
        self.buffer[self.row] = line[: self.col] + char + line[self.col :]
        self.col += 1


def open_terminal_editor(file_path: Path) -> None:
    def curses_main(stdscr) -> None:
        editor = Editor(stdscr, file_path)
        while True:
            editor.render()
            if not editor.update():
                break

    curses.wrapper(curses_main)
