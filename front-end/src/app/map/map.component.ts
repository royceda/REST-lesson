import { Component, NgZone } from '@angular/core';
import { MouseEvent } from '@agm/core';

import { AgmCoreModule, MapsAPILoader } from '@agm/core';

import { DataService } from '../data.service'

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent  {
  // google maps zoom level
  zoom: number = 5;
  
  // initial center position for the map
  lat: number = 49.0083899664;
  lng: number = 2.5384411;

  flights: flight[] = [
    {
      op_nb : "AF1000",
      origin : "CDG",
      destination : "MAD",
      ori_lat : 49.0083899664,
      ori_lng : 2.5384411,
      dst_lat : 40.4839361 ,
      dst_lng : -3.5679515
    },
    {
      op_nb : "AF8260",
      origin : "TLS",
      destination : "AMS",
      ori_lat : 43.634330796,
      ori_lng : 1.367331864,
      dst_lat : 52.3105386,
      dst_lng : 4.7682744
    }
  ]

  constructor(private data: DataService) { 
    this.data.getFlights().subscribe(data => {
      //this.flights = data as flight[];
      console.log("Response : ", data);
      this.data.getAirports().subscribe(world_data => {
        console.log("Response : ", world_data);
      });
    });
  }

  clickedMarker(label: string, index: number) {
    console.log(`clicked the marker: ${label || index}`)
  }
  
  /*mapClicked($event: MouseEvent) {
    this.markers.push({
      lat: $event.coords.lat,
      lng: $event.coords.lng,
      draggable: true
    });
  }*/
  
  //m is a marker
  markerDragEnd(m: any, $event: MouseEvent) {
    console.log('dragEnd', m, $event);
  }


}




export interface flight {
  op_nb : string;
  origin : string;
  destination : string;
  ori_lat : number,
  ori_lng : number;
  dst_lat : number;
  dst_lng : number;
}