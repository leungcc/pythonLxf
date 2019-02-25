def lazy_num(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax;
    return sum;

_sum = lazy_num(1,2,3,4,5)
print(_sum())