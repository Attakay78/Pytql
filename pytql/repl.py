from .colors import Color


HEADER = f"{Color.cyan}Welcome to Pytql REPL! We hope you enjoy your stay!{Color.color_terminate}" # Repl Header Text to display.
FOOTER = f"{Color.cyan}Thanks for visiting the Pytql REPL today!{Color.color_terminate}" #Repl Footer Text to display.


def default_repl(scope) -> None:
    """Default repl to run Pytql client. Non-interactive.

    Args:
        scope (_type_): Variable scope to expose to the repl.
    """
    print(HEADER)
    print("crtl-c to quit\n")

    success_color = lambda input: f"{Color.green}{input}{Color.color_terminate}"
    failure_color = lambda input: f"{Color.red}{input}{Color.color_terminate}"

    success = lambda input: success_color(input)
    failure = lambda input: failure_color(input)
    try:
        while True:
            try:
                _in = input(">>> ")
                try:
                    exec_result = success(eval(_in))
                    if exec_result != success_color("None"):
                        print(exec_result)
                except:
                    out = exec(_in)
                    if out != None:
                        exec_result = success(out)
                        if exec_result != success_color("None"):
                            print(exec_result)
            except Exception as e:
                print(failure(f"Error: {e}"))
    except KeyboardInterrupt as e:
        print(f"\n{FOOTER}")


def interactive_repl(scope) -> None:
    """Interactive repl to run Pytql client. Interactive but no autocomplete.

    Args:
        scope (_type_): Variable scope to expose to the repl.
    """
    from code import InteractiveConsole
    header = HEADER + "\n" + "crtl-d to quit\n"
    footer = FOOTER
    scope_vars = scope()
    InteractiveConsole(locals=scope_vars).interact(header, footer)


def ipython_repl(scope) -> None:
    """Interactive repl to run Pytql client. Supports autocomplete and autosuggestions.

    Args:
        scope (_type_): Variable scope to expose to the repl.
    """
    import IPython
    header = HEADER
    footer = FOOTER
    scope_vars = scope()
    print(header)
    IPython.start_ipython(argv=[], user_ns=scope_vars)
    print(footer)



class ReplType:
    """Class listing of repl types.
    """
    default_repl = default_repl
    interactive_repl = interactive_repl
    ipython_repl = ipython_repl



def start_client(module_name, repl_type:ReplType = ReplType.default_repl):
    """Function to start the Pytql client repl.

    Args:
        module_name (_type_): Name of the module Pytql is being run from.
        repl_type (_type_, optional): Repl type to use. Defaults to ReplType.default_repl.
    """
    import importlib

    mod = importlib.import_module(module_name)
    globals().update(mod.__dict__)
    print()
    repl_type(globals)
