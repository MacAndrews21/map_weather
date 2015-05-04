
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
        url: 'data/19000121-test-data-point-id.geojson'            
    }),
    style: createPointStyleFunction()
});

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



