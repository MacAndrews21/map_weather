var voronoi = new Voronoi();

var bbox = {
    xl: 0
    , xr: 800
    , yt: 0
    , yb: 600
};

var sites = [
    {x: 200, y: 200}
    , {x: 50, y: 250}
    , {x: 400, y: 100}
]

var diagramm = voronoi.compute(sites, bbox)

console.log(diagramm.vertices)
console.log(diagramm.edges)
console.log(diagramm.cells)
console.log(diagramm.execTime)
