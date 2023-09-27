import cProfile, pstats, io


def profile(func):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        profile = cProfile.Profile()
        profile.enable()
        return_value = func(*args, **kwargs)
        profile.disable()
        string_io = io.StringIO()
        sort_by = "cumulative"
        profile_stats = pstats.Stats(profile, stream=string_io).sort_stats(sort_by)
        profile_stats.print_stats()
        print(string_io.getvalue())
        return return_value

    return inner
