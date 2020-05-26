import trimesh
from models.layers.mesh import *
import argparse
import pathlib
from utils import *
import warnings


def run(args):
    xyz, _ = read_pts(args.i)

    m = trimesh.convex.convex_hull(xyz[:, :3])
    vs, faces = m.vertices, m.faces

    export(args.o, vs, faces)

    if args.blender:
        blender_rehull(args.o, args.o, args.blender_res, args.blender_path)
    else:
        inplace_manifold(args.o, args.manifold_res, args.manifold_path)

    num_faces = count_faces(args.o)
    if args.blender:
        num_faces /= 2
    num_faces = int(num_faces)
    if num_faces < args.faces:
        software = 'blender' if args.blender else 'manifold'
        warnings.warn(f'only {num_faces} faces where generated by {software}. '
                      f'try increasing --{software}-res to achieve the desired target of {args.faces} faces')
    else:
        inplace_simplify(args.o, args.faces, args.manifold_path)

    print('*** Done! ****')


def check_args(args):
    if not args.i.exists():
        raise FileNotFoundError('can\' find input file')

    if args.blender:
        if not (args.blender_path / 'blender').exists():
            raise FileNotFoundError('can\' find blender')
    else:
        if not (args.manifold_path / 'manifold').exists():
            raise FileNotFoundError('can\' find manifold software')

        if not (args.manifold_path / 'simplify').exists():
            raise FileNotFoundError('can\' find simplify software')

    if not args.o:
        args.o = args.i.with_name('.'.join(args.i.name.split('.')[:-1]) + '_hull.obj')
    else:
        args.o = Path(args.o)


def count_faces(path: Path) -> int:
    with open(path, 'r') as file:
        lines = file.read().split('\n')
    return sum(map(lambda x: x.startswith('f'), lines))


def inplace_manifold(path: Path, res: int, manifold_software_path: Path):
    cmd = f'{manifold_software_path}/manifold {path} {path} {res}'
    os.system(cmd)


def inplace_simplify(path: Path, faces: int, manifold_software_path: Path):
    cmd = f'{manifold_software_path}/simplify -i {path} -o {path} -f {faces}'
    os.system(cmd)


def blender_rehull(target: Path, dest: Path, res: int, blender_path: Path):
    base_path = pathlib.Path(__file__).parent.absolute()
    cmd = f'{blender_path}/blender --background --python {base_path}/blender_scripts/blender_hull.py' \
          f' {target} {res} {dest} > /dev/null 2>&1'
    os.system(cmd)


if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description='Convex hull maker')
    parser.add_argument('--i', type=Path, required=True,
                        help='path to read .xyz/.npts or .ply from')
    parser.add_argument('--faces', type=int, required=True, help='#target of faces for the convex hull')

    parser.add_argument('--o', type=str, required=False,
                        help='path to output convex hull obj to', default='')
    parser.add_argument('--manifold-path', type=Path, required=False,
                        help='path to build folder containing manifold and simplify software')
    parser.add_argument('--manifold-res', type=int, default=5000, required=False,
                        help='resolution for Manifold software')
    parser.add_argument('--blender', action='store_true')
    parser.add_argument('--blender-res', type=int, default=5, required=False,
                        help='resolution for making convex hulls with blender software')
    parser.add_argument('--blender-path', type=Path, required=False, help='path to folder containing blender')

    args = parser.parse_args()
    check_args(args)
    run(args)