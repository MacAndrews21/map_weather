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
/* bootstrap-slider */
var daySlider_2 = new Slider('input.daySlider_2', {
        formatter: function(value) {
                return 'Current value: ' + value;
        }
});

var yearSlider_2 = new Slider('input.yearSlider_2', {
        formatter: function(value) {
                return 'Current value: ' + value;
        }
});
var testSlider = new Slider("input.testSlider", { 
        id: "test"
        , min: 1
        , max: 3
        , value: 1
//         , step: 1
//         , formatter: function(value) {
//                 return 'year: ' + value;
//         }
//         , orientation: 'vertical'
//         , ticks: [1, 2, 3]
//         , ticks_snap_bounds: 30
        , handle: 'square' /* round, square, triangle, custom */ 
        , enabled: true
//         , range: true
       
});

/* dhtml-slider */
    var width = 300; //window.innerWidth - 200
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
    /* html 5 slider */
    var htmlSlider = document.getElementById("htmlSlider");
    htmlSlider.setAttribute("value", 1);
    htmlSlider.setAttribute("min", 1);
    htmlSlider.setAttribute("max", 3);
    htmlSlider.setAttribute("step", 1);
    
} // init()############################################################################################

