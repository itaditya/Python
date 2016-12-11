from rootFinderModule import rootFinder


def recur(a, b, f_a, f_b):
    return ((a + b) / 2)

finder = rootFinder(recur)
finder.input_params()
finder.expression_generator()
a, b = finder.initial_domain()
root = finder.root_finder(a, b)
finder.show_root()

print(finder.fn_evaluate(root))
