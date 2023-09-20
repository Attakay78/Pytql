from colorama import Fore, init

init(autoreset=True)

def default_repl(scope) -> None:
    print(f"{Fore.CYAN}Welcome to REPL! We hope you enjoy your stay!")
    print("crtl-c to quit")

    success_color = Fore.GREEN
    failure_color = Fore.RED

    success = lambda input: f"{success_color}{input}"
    failure = lambda input: f"{failure_color}{input}"
    try:
        while True:
            try:
                _in = input(">>> ")
                try:
                    exec_result = success(eval(_in))
                    if exec_result != f"{success_color}None":
                        print(exec_result)
                except:
                    out = exec(_in)
                    if out != None:
                        exec_result = success(out)
                        if exec_result != f"{success_color}None":
                            print(exec_result)
            except Exception as e:
                print(failure(f"Error: {e}"))
    except KeyboardInterrupt as e:
        print("\nExiting...")


def interactive_repl(scope) -> None:
    from code import InteractiveConsole
    header = "Welcome to REPL! We hope you enjoy your stay!"
    footer = "Thanks for visiting the REPL today!"
    scope_vars = scope()
    InteractiveConsole(locals=scope_vars).interact(header, footer)


def ipython_repl(scope) -> None:
    import IPython
    header = "Welcome to REPL! We hope you enjoy your stay!"
    footer = "Thanks for visiting the REPL today!"
    scope_vars = scope()
    print(header)
    IPython.start_ipython(argv=[], user_ns=scope_vars)
    print(footer)


class ReplType:
    default_repl = default_repl
    interactive_repl = interactive_repl
    ipython_repl = ipython_repl



def start_client(module_name, repl_type:ReplType = ReplType.default_repl):
    import importlib

    mod = importlib.import_module(module_name)
    globals().update(mod.__dict__)
    print()
    repl_type(globals)
