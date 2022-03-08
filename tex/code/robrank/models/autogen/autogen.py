import itertools as it
import rich
c = rich.get_console()

HM_TEMPLATE_RC2F2 = '''
from .. import rc2f2
import rich
c = rich.get_console()
class Model(rc2f2.Model):
    is_advtrain_hm = True
'''

HM_TEMPLATE_RRES18 = '''
from .. import rres18
import rich
c = rich.get_console()
class Model(rres18.Model):
    is_advtrain_hm = True
'''

HM_TEMPLATE_RRES50 = '''
from .. import rres50
import rich
c = rich.get_console()
class Model(rres50.Model):
    is_advtrain_hm = True
'''

HM_TEMPLATE_POST_INIT_HOOK = '''
    def post_init_hook(self):
        c.print('HM Specification')
        c.print(self.hm_spec)
'''

HM_TEMPLATES = [
    ('rc2f2', HM_TEMPLATE_RC2F2),
    ('rres18', HM_TEMPLATE_RRES18),
    ('rres50', HM_TEMPLATE_RRES50),
]

HARDNESS = ('r', 'm', 's', 'd', 'h')
HARDNESS_MAP = {'r': 'spc2-random', 'm': 'spc2-semihard',
                's': 'spc2-softhard', 'd': 'spc2-distance', 'h': 'spc2-hard'}


def write_model_config(filename, template, grad, r, hm, srch, desth, ics):
    pad = '    '
    end = '\n'
    with open(filename, 'wt') as f:
        f.write(template)
        f.write(pad + 'hm_spec = {' + end)
        f.write(pad * 2 + f"'hm': '{hm.upper()}'," + end)
        f.write(pad * 2 + f"'gradual': {g}," + end)
        f.write(pad * 2 + f"'fix_anchor': {r}," + end)
        f.write(pad * 2 + f"'srch': '{HARDNESS_MAP[srch]}'," + end)
        f.write(pad * 2 + f"'desth': '{HARDNESS_MAP[desth]}'," + end)
        f.write(pad * 2 + f"'ics': {ics}," + end)
        f.write(pad + '}' + end)
        f.write(HM_TEMPLATE_POST_INIT_HOOK + end)

init_py = open('__init__.py', 'wt')
init_py.write(f'# Automatically generated by {__file__}\n')

gitignore = open('.gitignore', 'wt')
gitignore.write(f'# Automatically generated by {__file__}\n')

count = 0
for (name, template) in HM_TEMPLATES:
    for g in (False, True):
        for r in (False, True):
            for hm in ('kl', 'l2', 'et'):
                for (srch, desth) in it.product(HARDNESS, HARDNESS):
                    for ics in (False, True):
                        filename = name
                        if g:
                            filename += 'g'
                        if r:
                            filename += 'rh'
                        else:
                            filename += 'hm'
                        filename += hm
                        filename += srch
                        filename += desth
                        if ics:
                            filename += 'i'
                        modulename = filename
                        filename += '.py'
                        with c.status('Creating ' + filename + ' ...'):
                            write_model_config(filename, template, g, r, hm, srch, desth, ics)
                        init_py.write(f'from . import {modulename}\n')
                        gitignore.write(f'{filename}\n')

                        count += 1

init_py.close()
gitignore.close()

c.print(f'* Written {count} model configuration files.')
