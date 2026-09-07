"""Transpone un archivo de ejercicios de Do mayor a Fa mayor usando el AST,
   tocando solo los valores de 'pitch', 'pitches' y 'label' (nombres de acorde),
   sin arriesgar el texto narrativo."""
import ast
from transpose_util import transpose_pitch

SOLFEGE_MAP = {'Do':'Fa','Re':'Sol','Mi':'La','Fa':'Sib','Sol':'Do','La':'Re','Si':'Mi'}
PITCH_RE = __import__('re').compile(r'^[A-G][#b]?[0-9]$')

class Transposer(ast.NodeTransformer):
    def visit_Dict(self, node):
        self.generic_visit(node)
        for i, k in enumerate(node.keys):
            if isinstance(k, ast.Constant) and k.value in ('pitch',):
                v = node.values[i]
                if isinstance(v, ast.Constant) and isinstance(v.value, str) and PITCH_RE.match(v.value):
                    node.values[i] = ast.Constant(value=transpose_pitch(v.value))
            if isinstance(k, ast.Constant) and k.value in ('pitches',):
                v = node.values[i]
                if isinstance(v, ast.List):
                    for j, elt in enumerate(v.elts):
                        if isinstance(elt, ast.Constant) and isinstance(elt.value, str) and PITCH_RE.match(elt.value):
                            v.elts[j] = ast.Constant(value=transpose_pitch(elt.value))
            if isinstance(k, ast.Constant) and k.value in ('label',):
                v = node.values[i]
                if isinstance(v, ast.Constant) and isinstance(v.value, str) and v.value in SOLFEGE_MAP:
                    node.values[i] = ast.Constant(value=SOLFEGE_MAP[v.value])
        return node

    def visit_Tuple(self, node):
        self.generic_visit(node)
        # Handle (['X3','Y3'], 'Label') tuples and ('X4', n) tuples used for finger patterns
        new_elts = []
        for idx, elt in enumerate(node.elts):
            if isinstance(elt, ast.List):
                for j, sub in enumerate(elt.elts):
                    if isinstance(sub, ast.Constant) and isinstance(sub.value, str) and PITCH_RE.match(sub.value):
                        elt.elts[j] = ast.Constant(value=transpose_pitch(sub.value))
            elif isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                if PITCH_RE.match(elt.value) and idx == 0:
                    node.elts[idx] = ast.Constant(value=transpose_pitch(elt.value))
                elif elt.value in SOLFEGE_MAP and idx >= 1:
                    node.elts[idx] = ast.Constant(value=SOLFEGE_MAP[elt.value])
        return node

def transpose_file(src_path, dst_path):
    src = open(src_path).read()
    tree = ast.parse(src)
    new_tree = Transposer().visit(tree)
    ast.fix_missing_locations(new_tree)
    new_src = ast.unparse(new_tree)
    open(dst_path, 'w').write(new_src)

if __name__ == '__main__':
    import sys
    transpose_file(sys.argv[1], sys.argv[2])
    print('transposed', sys.argv[1], '->', sys.argv[2])
