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
                ,pointJSON
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
 * Styled in slider-style.css 
 * Slider functionality is defined in slider.js
 */
    var voronoi_id = 1
    var layers = map.getLayers()
    
    var yourSites = [];
//     console.log(pointJSON)
//     console.log(pointJSON.getSource().getExtent())
//     function getCoord() {
//         pointJSON.getSource().getFeatures().forEach(function(pJ){
// //             console.log("Stationsname: " + pJ.getProperties()['stationsname'])
//             console.log("Geometry: ", pJ.getGeometry())
// //             console.log("Geometry Type: " + pJ.getGeometry().getType())
//             console.log("Geometry Coordinates: " + pJ.getGeometry().getCoordinates())
// //             console.log("Geometry Name: " + pJ.getGeometryName())
// // //             console.log("Extent: ", pJ.getExtent())
// //             console.log("Feature ID: " + pJ.getId())
//             yourSites.push(pJ.getGeometry().getCoordinates())
//     console.log(yourSites)
//         })
//         
//     }
//     getCoord(pointJSON)
//     console.log(pointJSON.getSource().getFeatures().length)
// console.log("F-ID: " + pointJSON.getSource().getFeatureById(02))
// console.log(pointJSON.getSource().getAttributions())
    var sitesID = 1
       var consoleSliderDHTMLX = new dhtmlXSlider({
        parent: "console-slider-dhtmlx", 
        size: 300,
        min: 1,
        max: 3, 
        step: 1
    
    }); 
    layersSites.getCoord(pointJSON);
     consoleSliderDHTMLX.attachEvent("onChange", function(){
//             console.log(horizontalSliderDHTMLX.getValue())
            sitesID = consoleSliderDHTMLX.getValue()
            if (sitesID == 1){
//                 layers.pop()
//                 map.addLayer(voronoi_1)
                   layersSites.getCoord(pointJSON);
            } else if (sitesID == 2) {
//                 layers.pop()
//                 map.addLayer(voronoi_2)
//                 layersSites.getCoord(pointJSON);
//                 test(pointJSON)
                layersSites.init(pointJSON);
            } else if (sitesID == 3) {
//                 layers.pop()
//                 map.addLayer(voronoi_3)
                layersSites.getCoord(pointJSON);
            }
        });   
/* dhtml-slider */
    var horizontalSliderDHTMLX = new dhtmlXSlider({
        parent: "horizontal-slider-dhtmlx", 
        size: 300,
        min: 1,
        max: 3, 
        step: 1
    
    });
    var verticalSliderDHTMLX = new dhtmlXSlider({
        parent: "vertical-slider-dhtmlx", 
        size: 300,
        min: 1,
        max: 3, 
        step: 1,
        vertical: true
    
    });
    
    horizontalSliderDHTMLX.attachEvent("onChange", function(){
//             console.log(horizontalSliderDHTMLX.getValue())
            voronoi_id = horizontalSliderDHTMLX.getValue()
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
    verticalSliderDHTMLX.attachEvent("onChange", function(){
//             console.log(verticalSliderDHTMLX.getValue())
            voronoi_id = verticalSliderDHTMLX.getValue()
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
/* bootstrap-slider */
    var horizontalSliderBootstrap = new Slider("input#horizontal-slider-bootstrap", { 
        id: "horizontal-slider-bootstrap"
        , min: 1
        , max: 3
        , value: 1
        , step: 1
        , handle: 'round' /* round, square, triangle, custom */ 
        , enabled: true
        , width: 300
       
    });
    var verticalSliderBootstrap = new Slider("input#vertical-slider-bootstrap", { 
        id: "vertical-slider-bootstrap"
        , min: 1
        , max: 3
        , value: 1
        , step: 1
        , handle: 'round' /* round, square, triangle, custom */ 
        , enabled: true
        , height: 300
        , orientation: "vertical"
       
    });
    horizontalSliderBootstrap.on("change", function(){
    //     console.log(horizontalSliderBootstrap.getValue());
        voronoi_id = horizontalSliderBootstrap.getValue()
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
        
    })
    verticalSliderBootstrap.on("change", function(){
    //     console.log(verticalSliderBootstrap.getValue());
        voronoi_id = verticalSliderBootstrap.getValue()
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
        
    })


    
    
    
    /* html 5 slider */
    var horizontalHTMLSlider = document.getElementById("horizontal-htmlSlider");
    horizontalHTMLSlider.setAttribute("value", 1);
    horizontalHTMLSlider.setAttribute("min", 1);
    horizontalHTMLSlider.setAttribute("max", 3);
    horizontalHTMLSlider.setAttribute("step", 1);

    var verticalHTMLSlider = document.getElementById("vertical-htmlSlider");
    verticalHTMLSlider.setAttribute("value", 1);
    verticalHTMLSlider.setAttribute("min", 1);
    verticalHTMLSlider.setAttribute("max", 3);
    verticalHTMLSlider.setAttribute("step", 1); 
//     verticalHTMLSlider.setAttribute("orient", "vertical"); // not working
//     horizontalHTMLSlider.setAttribute("style", "background-color:#FE9A2E");

    horizontalHTMLSlider.oninput = function(){
//             console.log(horizontalHTMLSlider.value);
            voronoi_id = horizontalHTMLSlider.value
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
    }
    verticalHTMLSlider.oninput = function(){
//             console.log(verticalHTMLSlider.value);
            voronoi_id = verticalHTMLSlider.value
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
    } 
    
//     var output = document.createElement("DIV");
//     output.setAttribut("id", "output");
//     document.getElementById("output").innerHTML = "test"
//     
    
} // init()############################################################################################

