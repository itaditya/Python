import rootFinderModule


def recur(a, b, f_a, f_b):
    return ((a * f_b - b * f_a) / (f_b - f_a))

finder = rootFinderModule.rootFinder(recur)
finder.input_params()
finder.expression_generator()
a, b = finder.initial_domain()
root = finder.root_finder(a, b)
finder.show_root()
