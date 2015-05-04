// var voronoi = new Voronoi();
// 
// var bbox = {
//     xl: 0
//     , xr: 800
//     , yt: 0
//     , yb: 600
// };
// 
var sites = [
    {x: 200, y: 200}
    , {x: 50, y: 250}
    , {x: 400, y: 100}
]
// 
// var diagramm = voronoi.compute(sites, bbox)

// console.log(diagramm.vertices)
// console.log(diagramm.edges)
// console.log(diagramm.cells)
// console.log(diagramm.execTime)
// function getSites(fileName){
//     var mySites = []
// 
//     var jsonFile = $.getJSON(fileName,function(json){  
//         var features = json.features  
//         return features
//         //         console.log(json)
// //         var x1 = json.features[0].geometry.coordinates[0]
// //         var y1 = json.features[0].geometry.coordinates[1]
// //         var x2 = json.features[1].geometry.coordinates[0]
// //         var y2 = json.features[1].geometry.coordinates[1]
// //         mySites = [
// //         {x: x1, y: y1}
// //         , {x: x2, y: y2}]
// // 
// //         console.log(x1)
// //         console.log(y1)
// //         console.log(x2)
// //         console.log(y2)
// //         $("#tempData").append(mySites);
// //         $("#tempData").hide();
//     })
// //         mySites.push("Welt")
// //         my = document.getElementById("tempData").value;
//         console.log(jsonFile)
// //         console.log(jsonFile)
//         return mySites
// }
// getSites("data/19000121-test-data-point.geojson")
// console.log(map.pointJSON.getGeometry())
// getCoord(pointJSON)

var VoronoiDemo = {
    voronoi: new Voronoi(),
//     sites: [
//         {x: 200, y: 200}
//         , {x: 50, y: 250}
//         , {x: 400, y: 100}
//         , {x: 300, y: 100}
//         , {x: 300, y: 200}
//         , {x: 700, y: 500}
//     ],
    sites: sites,
    diagram: null,
    margin: 0.15,
    canvas: null,
    bbox: {xl:0,xr:800,yt:0,yb:600},
    init: function() {
        this.canvas = document.getElementById('voronoiCanvas');
        this.diagram = this.voronoi.compute(this.sites, this.bbox);
//         this.randomSites(0,false);
//         this.sites.getSites("data/19000121-test-data-point.geojson")
//         getCoord(pointJSON);
        init();
        this.render();
        },
//     getSites
    
    render: function() {
        var ctx = this.canvas.getContext('2d');
        // background
        ctx.globalAlpha = 1;
        ctx.beginPath();
        ctx.rect(0,0,this.canvas.width,this.canvas.height);
        ctx.fillStyle = 'white';
        ctx.fill();
        ctx.strokeStyle = '#888';
        ctx.stroke();
        // voronoi
        if (!this.diagram) {return;}
        // edges
        ctx.beginPath();
        ctx.strokeStyle = '#000';
        var edges = this.diagram.edges,
            iEdge = edges.length,
            edge, v;
        while (iEdge--) {
            edge = edges[iEdge];
            v = edge.va;
            ctx.moveTo(v.x,v.y);
            v = edge.vb;
            ctx.lineTo(v.x,v.y);
            }
        ctx.stroke();
        // edges
        ctx.beginPath();
        ctx.fillStyle = 'red';
        var vertices = this.diagram.vertices,
            iVertex = vertices.length;
        while (iVertex--) {
            v = vertices[iVertex];
            ctx.rect(v.x-1,v.y-1,3,3);
            }
        ctx.fill();
        // sites
        ctx.beginPath();
        ctx.fillStyle = '#44f';
        var sites = this.sites,
            iSite = sites.length;
        while (iSite--) {
            v = sites[iSite];
            ctx.rect(v.x-2/3,v.y-2/3,2,2);
            }
        ctx.fill();
        }
}