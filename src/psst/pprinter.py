from click import echo, style

def p_print(arr: list) -> None:

    echo(f'{style("Ports:", fg="yellow")}')

    if len(arr) == 0:
        echo(f'{" " * 4}{style("None", fg="red")}')
    else:
        for port in arr:
            echo(f'{" " * 4}Port: {style(port, fg="green")}')

    
    echo("\n")
    
    pass