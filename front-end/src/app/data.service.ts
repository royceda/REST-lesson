import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})
export class DataService {

  url: string = " "

  constructor(private _http: HttpClient) { }

  getFlights() {
    return this._http.get("http://127.0.0.1:7777/flights")
  }
  
  getAirports(){
    return this._http.get("../assets/airports.json")
  }



}
