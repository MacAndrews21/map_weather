/**
 * -------------------------------------------------------------------------------------------------------
 * style for points [stations]
 * -------------------------------------------------------------------------------------------------------
 */
var createPointStyleFunction = function(){
    return function(feature, resolution){
        var style = new ol.style.Style({
            image: new ol.style.Circle({
                        radius: 2,
                        fill: new ol.style.Fill({
                            color: 'red'
                        }),
                        stroke: new ol.style.Stroke({
                            color: 'red', 
                            width: 2        
                        })    
                    })
        });
    return [style]    
    };
};

/**
 * -------------------------------------------------------------------------------------------------------
 * style for polygons [voronoi]
 * -------------------------------------------------------------------------------------------------------
 */
var setFillColor = function(feature, resolution){
    var luft = feature.get('lufttemper');
//     console.log(luft);
    if ( luft <= 0){
        var color = 'rgba(0,0,255, 0.5)'
    }else if(luft > 0){
        var color = 'rgba(255,0,0, 0.5)'        
    }
    return color
}

var createPolygonStyleFunction = function(){
   return function(feature, resolution){
       var style = new ol.style.Style({
            stroke: new ol.style.Stroke({
                color: 'rgba(0,0,0,0.2)',
                width: 2
            }),
            fill: new ol.style.Fill({
                color:setFillColor(feature, resolution)                
            }),
            text: new ol.style.Text({
                font: '12px Calibri,sans-serif',
                fill: new ol.style.Fill({
                    color: '#000'
                }),
                stroke: new ol.style.Stroke({
                    color: '#fff',
                width: 3
                })
            })
            
        });
       style.getText().setText(resolution < 500 ? feature.get('lufttemper') : '');
//        style.getText().setFill
       return [style]
   };
};
/**
 * -------------------------------------------------------------------------------------------------------
 * style for polygons [germany boundaries]
 * -------------------------------------------------------------------------------------------------------
 */
var boundariesStyleFunction = function(){
   return function(feature, resolution){
       var style = new ol.style.Style({
            stroke: new ol.style.Stroke({
                color: 'rgba(0,0,0,0.9)',
                width: 2
            }),
            fill: new ol.style.Fill({
                color: 'rgba(125,125,125,1)'
            })
        });
       return [style]
   };
};




/**
 * style for text
 */















