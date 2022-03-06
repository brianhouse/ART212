- grade projects!

/


- photogrammetry
- EinScan-SE
- Structure Scanner


- meshmixer
- TinkerCad

- create 3D printer flow (and update firmware)



## Notes


### Photogrammetry

imagemagick can bulk convert heic
```
brew install imagemagick
mogrify -format jpg *.heic
```

Regard3D
- Add Images
- Compute Matches
- Triangulate
http://www.regard3d.org/index.php/documentation/tutorial


talk about:
point cloud vs mesh vs GCode

Meshmixer tutorial
https://all3dp.com/2/meshmixer-tutorial-easy-steps-beginners/

#### Meshmixer procedure
- discard jpg
- import (replace)
- show wireframe
- Edit: transform
- Edit: plane cut
- Edit: close cracks!
- Edit: Separate Shells
- Select: lasso and X other hanging bits, especially from the inside
- adjust size of select (down) -- escape cancels, x deletes

- alternate with separate shells

- use the inspector, click on the purple and
- get to the point that you can then Edit: make solid


Brushes: robust smooth

planecut on the bottom again to make sure it's flat

export as STL


### EinScan SE
