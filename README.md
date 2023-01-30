# Voronoi.py
Voronoi Diagrams in Python.

## Euclidean Distance
<p align="center">
    <img src=./out/euclidean.png width="100%"></img>
</p>

## Manhattan Distance
<p align="center">
    <img src=./out/manhattan.png width="100%"></img>
</p>

## Quick Start
* Clone the repo.
```bash
$ git clone https://github.com/orhanemree/voronoi.py.git
$ cd voronoi.py
```
* After installed the requirements, run the program.
```bash
$ python main.py
```

Note: Requirement `Pillow` is needed for only converting `.ppm` output to `.png`. Main Voronoi algorithm saves output as `.ppm` without any requirement. See [create.py](./create.py) for more details. You can change width, height, cell_count, distance_type and show_points values in [main.py](./main.py) to see different outputs.

## References
* [Voronoi Diagrams](https://en.wikipedia.org/wiki/Voronoi_diagram)
* [tsoding/voronoi-opengl](https://github.com/tsoding/voronoi-opengl)

## License
* Licensed under the [MIT License](./LICENSE).