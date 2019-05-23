import { Component, NgZone } from '@angular/core';
import { MouseEvent } from '@agm/core';

import { AgmCoreModule, MapsAPILoader } from '@agm/core';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent  {
  // google maps zoom level
  zoom: number = 9;
  
  // initial center position for the map
  lat: number = 51.673858;
  lng: number = 7.815982;

  polylines: Array<any> = [      
    {
    latitude:  39.8282,
    longitude: -98.5795,
    speed: 50
    },
    {
    latitude:  38.8282,
    longitude: -108.5795,
    speed: 50
    }
  ]

  constructor(    
    private mapsAPILoader: MapsAPILoader,
    private ngZone: NgZone){}

  clickedMarker(label: string, index: number) {
    console.log(`clicked the marker: ${label || index}`)
  }
  
  mapClicked($event: MouseEvent) {
    this.markers.push({
      lat: $event.coords.lat,
      lng: $event.coords.lng,
      draggable: true
    });
  }
  
  markerDragEnd(m: marker, $event: MouseEvent) {
    console.log('dragEnd', m, $event);
  }

  markers: marker[] = [
	  {
		  lat: 51.673858,
		  lng: 7.815982,
		  label: 'A',
		  draggable: true
	  },
	  {
		  lat: 51.373858,
		  lng: 7.215982,
		  label: 'B',
		  draggable: false
	  },
	  {
		  lat: 51.723858,
		  lng: 7.895982,
		  label: 'C',
		  draggable: true
	  }
  ]
}

// just an interface for type safety.
interface marker {
	lat: number;
	lng: number;
	label?: string;
	draggable: boolean;
}
