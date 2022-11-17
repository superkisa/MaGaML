# %%
from difflib import SequenceMatcher
from operator import itemgetter


class HintMixin:
    def __getattr__(self, name):
        candidates = []
        max_cand = (0.4, None)
        for attr in dir(self):
            ratio = SequenceMatcher(None, name, attr).ratio()
            if ratio > max_cand[0]:
                max_cand = (ratio, attr)
            if ratio > 0.6:
                candidates.append((ratio, attr))
        if not candidates and max_cand[1] is None:
            error_str = ''
        elif not candidates:
            error_str = f'Did you mean: {max_cand[1]}?'
        else:
            candidates.sort(reverse=True)
            candidates = ' / '.join(map(itemgetter(1), candidates))
            error_str = f'Did you mean: {candidates}?'

        raise AttributeError(f'\'{self.__class__.__name__}\' object has \
            no attribute \'{name}\'. {error_str}')


class NumberGenerator(HintMixin):

    def __init__(self):
        pass

    def generate_number(self):
        return 9

    def generate_number99(self):
        return 99

    def generate_cat(self):
        return '🙀'

    def generate_big_number(self):
        return 9999
    
    def do_nothing(self):
        ...


ng = NumberGenerator()
ng.generate_n123ber()


# %%
