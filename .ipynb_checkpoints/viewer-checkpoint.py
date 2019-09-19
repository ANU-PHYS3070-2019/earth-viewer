def new_viewer(topo_file):
       
    import numpy as np
    import imageio, PIL.Image
    import stripy, lavavu
    
    print("Building spherical mesh ", flush=True)
    
    res_lon = 1800
    res_lat = 900
    mesh = stripy.hybrid_st_meshes.warped_xy_mesh_sphere(res_lon=res_lon, res_lat=res_lat)

    print("Reading topography data file  ", flush=True)

    topography_data = np.array(imageio.imread(topo_file))

    height = np.array(PIL.Image.fromarray(topography_data.view()).resize((res_lon,res_lat))).astype(float)
    hrange = height.max()-height.min()
    height0 = (height - height.min()) / hrange 


    XX = mesh.XX
    YY = mesh.YY
    ZZ = mesh.ZZ
    
    print("Building 3D viewer ")

    lv1 = lavavu.Viewer(border=False, resolution=[1066,666], background="#FFFFFF")
    lv1["axis"]=False
    lv1['specular'] = 0.1

    shrink_surface = 1.0  + 0.05 * height0.reshape(-1)

    tris1 = lv1.triangles("surfacemap",  wireframe=False, colour="#000000:0.0")
    tris1.vertices([XX*shrink_surface, YY*shrink_surface, ZZ*shrink_surface])
    tris1.indices(mesh.simplices)
    tris1.texcoords([mesh.SS,mesh.TT])

    from matplotlib import cm
    from matplotlib.colors import Normalize
    
    print("Laying down topography image")

    terrain_norm = Normalize(vmin=-5000.0, vmax=10000.0)
    texdata = cm.terrain(terrain_norm(topography_data))
    tris1.texture(texdata, flip=False)
    
    print("Launching 3D viewer")

    lv1.window(menu=False)
    
    return lv1

    