/**
 * global variable 'map'
 */
var map;
/**
 * $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 * function to build things after site is loaded
 */
function init(){
/**
 * ----------------------------------------------------------------------------------------------------
 * MAP
 */    
    map = new ol.Map({
            layers: [
//                 mapQuest  // mapQuest topographic background map
                boundaries_europe
                ,boundaries_germany // germany boundaries
                ,voronoi_1
            ],
            view: new ol.View({
                center: ol.proj.transform([11, 51], 'EPSG:4326', 'EPSG:3857'),
                zoom: 6 
//                 extent:[9,50 12,52]
            }),
            target: 'map'
        });

/**
 * ----------------------------------------------------------------------------------------------------
 * SLIDER
 */
    var width = 30; //window.innerWidth - 200
    var daySlider = new dhtmlXSlider({
        parent: "daySlider", 
        size: width,
        min: 1,
        max: 3, 
        step: 1
    
    });
    var yearSlider = new dhtmlXSlider({
        parent: "yearSlider", 
        size: width,
        min: 1,
        max: 3, 
        step: 1,
        vertical: true
    
    });
    
    var voronoi_id = 1
    daySlider.attachEvent("onChange", function(){
//             console.log(daySlider.getValue())
            var layers = map.getLayers()
            voronoi_id = daySlider.getValue()
            if (voronoi_id == 1){
                layers.pop()
                map.addLayer(voronoi_1)
            } else if (voronoi_id == 2) {
                layers.pop()
                map.addLayer(voronoi_2)
            } else if (voronoi_id == 3) {
                layers.pop()
                map.addLayer(voronoi_3)
            }
        });

    
} // init()############################################################################################

