import yaml
from glob import glob
import treegraph
from treegraph.scripts import tree2qsm

## set input candidates
# path to tree point cloud, str
data_path = '../../data/ww_1361w.ply'
# index of base point, int, default None
base_idx = None
# file saving attribute, str, default 'nbranch'
attribute = 'nbranch'
# 'sf_radius': surface fitting radius, 'm_radius': smoothed radius
radius = ['m_radius']
# print something
verbose = False
# voxel length for downsample when generating initial graph
cluster_size = .04
# min number of points to pass the filtering
minpts = 5
# the base of the exponential function which segments the inital graph
exponent = [2]
# min length of a segmented slice
minbin = [.03, .04]
# max length of a segmented slice
maxbin = [.25, .30]
# path to outputs
output_path = '../../results/ww_1361w_v1.6/'


## generate yaml files to store each combination of inputs
for i in range(len(radius)):
    for j in range(len(exponent)):
        for k in range(len(minbin)):
            for l in range(len(maxbin)):
                inputs = {'data_path':data_path,
                          'base_idx':base_idx,
                          'attribute':attribute,
                          'radius':radius[i],
                          'verbose':verbose,
                          'cluster_size':cluster_size,
                          'minpts':minpts,
                          'exponent':exponent[j],
                          'minbin':minbin[k],
                          'maxbin':maxbin[l],
                          'output_path':output_path}
                with open(f'../IO/inputs_{radius[i]}_e{exponent[j]}_minbin{minbin[k]}_maxbin{maxbin[l]}.yml', 'w') as f:
                    f.write(yaml.safe_dump(inputs))


## batch run treegraph
inputs_f = glob('../IO/inputs_*.yml')
for m in range(len(inputs_f)):
    with open (inputs_f[m]) as fr:
        args = yaml.safe_load(fr)
        for key, item in args.items():
            print(f'{key}: {item}')
        
    tree2qsm.run(args['data_path'], 
                base_idx=args['base_idx'],
                attribute=args['attribute'], 
                radius=args['radius'], 
                verbose=args['verbose'],
                cluster_size=args['cluster_size'], 
                min_pts=args['minpts'], 
                exponent=args['exponent'], 
                minbin=args['minbin'],
                maxbin=args['maxbin'],
                output=args['output_path'])
