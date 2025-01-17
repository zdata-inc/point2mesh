<img src='docs/images/lizard2.gif' align="right" width=325>
<br><br><br>

# Point2Mesh in PyTorch


### SIGGRAPH 2020 [[Paper]](https://arxiv.org/abs/2005.11084) [[Project Page]](https://ranahanocka.github.io/point2mesh/)<br>

Point2Mesh is a technique for reconstructing a surface mesh from an input point cloud.
This approach "learns" from a single object, by optimizing the weights of a CNN to deform some initial mesh to shrink-wrap the input point cloud.
The argument for going this route is: since the (local) convolutional kernels are optimized globally across the entire shape,
this encourages local-scale geometric self-similarity across the reconstructed shape surface.

<img src="docs/images/global_anky.gif" align="center" width="250px"> <br>

The code was written by [Rana Hanocka](https://www.cs.tau.ac.il/~hanocka/) and [Gal Metzer](https://www.linkedin.com/in/gal-metzer-512803a1/).

# Getting Started

### Installation
#### Clone this repo:
```bash
git clone https://github.com/zdata-inc/point2mesh.git

cd point2mesh

git submodule init
```

#### Setup with Conda
Refer to the [PyTorch3D repo](https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md) for complete
installation instructions

```bash
conda create -n point2mesh python=3.9
conda activate point2mesh
conda install pytorch=1.13.0 torchvision pytorch-cuda=11.6 -c pytorch -c nvidia
conda install -c fvcore -c iopath -c conda-forge fvcore iopath
pip install "git+https://github.com/facebookresearch/pytorch3d.git@stable"
pip install trimesh
# pip install bpy -- requires python 3.10 or python < 3.8
```

#### Setup without Conda
```bash
python3 -m venv point2mesh
pip install torch==1.13.0 torchvision
pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116
pip install "git+https://github.com/facebookresearch/pytorch3d.git@stable"
pip install trimesh
```

#### Install "Manifold" Software on Linux
Refer to the [Manifold repo](https://github.com/zdata-inc/Manifold) for complete installation instructions.

```bash
cd Manifold
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make
```

#### Install "Manifold" Software on Windows
```bash
cd Manifold
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --target Manifold --config Release
```

# Running Examples
 
### Get Data
Download our example data
```bash
bash ./scripts/get_data.sh
```

### Running Reconstruction 
First, if using conda env first activate env e.g. ```source activate point2mesh```.
All the scripts can be found in ```./scripts/examples```.
Here are a few examples:

#### Giraffe
```bash
bash ./scripts/examples/giraffe.sh
```

#### Bull
```bash
bash ./scripts/examples/bull.sh
```

#### Tiki
```bash
bash ./scripts/examples/tiki.sh
```

#### Noisy Guitar
```bash
bash ./scripts/examples/noisy_guitar.sh
```
... and more.
#### All the examples
To run all the examples in this repo:
```bash
bash ./scripts/run_all_examples.sh
```
# Running different Examples
You should provide an initial mesh file. If the shape has genus 0, you can use the convex hull script provided in ```./scripts/process_data/convex_hull.py```

# Citation
If you find this code useful, please consider citing our paper
```
@article{Hanocka2020p2m,
  title = {Point2Mesh: A Self-Prior for Deformable Meshes},
  author = {Hanocka, Rana and Metzer, Gal and Giryes, Raja and Cohen-Or, Daniel},
  year = {2020},
  issue_date = {July 2020}, 
  publisher = {Association for Computing Machinery}, 
  volume = {39}, 
  number = {4}, 
  issn = {0730-0301},
  url = {https://doi.org/10.1145/3386569.3392415},
  doi = {10.1145/3386569.3392415},
  journal = {ACM Trans. Graph.}, 
}
```

# Questions / Issues
If you have questions or issues running this code, please open an issue.
