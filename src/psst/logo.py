from click import clear, echo, style

def draw_logo() -> None:
    cat_row_1 = " _._     _,-'""`-._"
    cat_row_2 = "(,-.`._,'(       |\`-/|"
    cat_row_3 = "    `-.-' \ )-`( , o o)"
    cat_row_4 = """          `-    \`_`"'-"""
    clear()
    echo(f'{style("-" * 48, fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 46}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 20} PSST {" " * 20}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 10} Port Super Scanner Tool {" " * 11}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 46}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 11}{style(cat_row_1, fg="red")}{" " * 18}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 11}{style(cat_row_2, fg="red")}{" " * 12}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 11}{style(cat_row_3, fg="red")}{" " * 12}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 11}{style(cat_row_4, fg="red")}{" " * 12}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 20}By: Kleo Hasani {" " * 10}{style("#", fg="blue")}')
    echo(f'{style("-" * 48, fg="blue")}')
    pass