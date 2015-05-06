
/** 
 * ---------------------------------------------------------------------------------------------------- 
 * background map from open-street-map
 */
var mapQuest = new ol.layer.Tile({
    style: 'Road',
    source: new ol.source.MapQuest({
        layer: 'osm'
    })    
});

/**
 * ---------------------------------------------------------------------------------------------------- 
 * load geoJson point file
 */
var vector = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        projection: 'EPSG:3857',
        url: 'data/test-data.geojson'            
    }),
    style: createPointStyleFunction()
});

var pointJSON = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        projection: 'EPSG:3857',
        url: 'data/19000121-test-data-point.geojson'            
    }),
    style: createPointStyleFunction()
});
var anitaSites = [];
var bbox = [];
var layersSites = {
//     pointJSON: pointJSON,
    say: function (){
        console.log("Hallo Welt")
    },
    voronoi: new Voronoi(),
    sites: [],
    bbox: {
        xl:     677189.86
        , xr:   1606707.61
        , yt:   7300603.61
        , yb:   6073828.52
    },
    diagram: null,
    init: function(t){
        this.sites = this.getCoord(t);
        console.log(this.bbox);
        console.log(this.bbox["xl"]);
        console.log(this.sites);
//        console.log(this.voronoi.compute(this.sites, this.bbox));
        this.diagram = this.voronoi.compute(this.sites, this.bbox);
        console.log(this.diagram.vertices)
        console.log(this.diagram.edges)
        console.log(this.diagram.cells)
        console.log(this.diagram.execTime)
    },
    getCoord: function(layer){
        anitaSites = [];
        layer.getSource().getFeatures().forEach(function(pJ){
//             console.log("Stationsname: " + pJ.getProperties()['stationsname'])
//             anitaSites.push(pJ.getGeometry().getCoordinates())
//             console.log("X: ", pJ.getGeometry().getCoordinates()[0])
//             console.log("Y: ", pJ.getGeometry().getCoordinates()[1])
            var x = pJ.getGeometry().getCoordinates()[0];
            var y = pJ.getGeometry().getCoordinates()[1];
            if (x < this.bbox["xl"]){
                console.log("x < xl", x, this.bbox["xl"])
            }
            if (x > this.bbox["xr"]){
                console.log("x > xr", x, this.bbox["xr"])
            }
            if (y < this.bbox["yb"]){
                console.log("y < yb", y, this.bbox["yb"])
            }
            if (y > this.bbox["yt"]){
                console.log("y > yt", y, this.bbox["yt"])
            }
            anitaSites.push({
                x: pJ.getGeometry().getCoordinates()[0],
                y: pJ.getGeometry().getCoordinates()[1]
                
            })
        })
//         console.log(pointJSON.getSource().getExtent())
//         console.log(anitaSites)
        return anitaSites
    }
}
function test(layer){
    console.log(layersSites.getCoord(layer))
// console.log(layersSites.getCoord(pointJSON))
}
/**
 * ---------------------------------------------------------------------------------------------------- 
 * load geoJson polygon file
 */
/**
 * ########################
 * boundaries of germany [simpified]
 */
var boundaries_germany = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        projection: 'EPSG:3857',
        url: 'data/germany-boundaries.geojson'            
    }),
    style: boundariesStyleFunction()
});
/**
 * ########################
 * boundaries of europe [simpified]
 */
var boundaries_europe = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        projection: 'EPSG:3857',
        url: 'data/europe.geojson'            
    }),
    style: boundariesStyleFunction()
});
/**
 * ########################
 * voronoi polygons 
 */
var voronoi_1 = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        projection: 'EPSG:3857',
        url: 'data/19000121-test-data-voronoi.geojson'            
    }),
    style: createPolygonStyleFunction()
});
var voronoi_2 = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        projection: 'EPSG:3857',
        url: 'data/19450121-test-data-voronoi.geojson'            
    }),
    style: createPolygonStyleFunction()
});
var voronoi_3 = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        projection: 'EPSG:3857',
        url: 'data/19820121-test-data-voronoi.geojson'            
    }),
    style: createPolygonStyleFunction()
});



